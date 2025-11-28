# "Histories of" Python Libraries and Resources

## Self-Learning PDF Tagger with Syntax-Based Prediction

You want a bot that:
1. **Starts with a known tag dictionary** (your "known universe")
2. **Learns syntactic patterns** around those known tags in context
3. **Predicts new tags** based on learned rules
4. **Self-validates** against the known universe to approach 99% accuracy

---

## Table of Contents
- High-Level Architecture
- Stack Recommendation (with program suggestions)
- Training Loop (how it learns and self-corrects)
- Implementation Phases
- Obsidian Integration (optional)
- Next Steps

---

## High-Level Architecture

```
┌─────────────────┐
│  Incoming PDFs  │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│  Text Extraction        │
│  (PyMuPDF / pdfplumber) │
└────────┬────────────────┘
         │
         ▼
┌──────────────────────────────┐
│  Syntax Parser & Embedder    │
│  (spaCy / transformer model) │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────────────┐
│  Pattern Learner                     │
│  - Finds co-occurrence patterns      │
│  - Learns syntactic context rules    │
│  - Builds predictive model           │
└────────┬─────────────────────────────┘
         │
         ▼
┌──────────────────────────────────┐
│  Tag Predictor                   │
│  - Guesses tags for new text     │
│  - Assigns confidence scores     │
└────────┬─────────────────────────┘
         │
         ▼
┌──────────────────────────────────┐
│  Self-Validation Loop            │
│  - Compares predictions to known │
│  - Updates model weights         │
│  - Logs accuracy metrics         │
└────────┬─────────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│  Tagged PDF Database         │
│  (SQLite / PostgreSQL)       │
│  + Obsidian markdown export  │
└──────────────────────────────┘
```

---

## Stack Recommendation

| Component | What It Does | Suggested Programs |
|-----------|--------------|-------------------|
| **PDF Text Extraction** | Pull raw text from PDFs | **PyMuPDF** (fast), **pdfplumber** (tables), **OCR**: Tesseract if scanned |
| **Syntax Parsing** | Identify parts of speech, dependencies, sentence structure | **spaCy** (industrial-strength NLP), **NLTK** (lighter), **Stanza** (multilingual) |
| **Embeddings / Context** | Turn words/sentences into vectors that capture meaning | **sentence-transformers** (all-MiniLM-L6-v2 is fast), **OpenAI embeddings API**, **spaCy's built-in vectors** |
| **Pattern Learning** | Learn co-occurrence and syntactic rules | **scikit-learn** (Naive Bayes, logistic regression), **LightGBM** (gradient boosting), or **simple Markov chains / n-grams** for syntax |
| **Self-Validation** | Compare predictions to known tags, update model | Custom Python loop with **accuracy tracking**, **confusion matrix** (scikit-learn), **active learning** framework |
| **Database** | Store PDFs, tags, metadata, accuracy logs | **SQLite** (local, simple), **PostgreSQL** (scalable), **DuckDB** (fast analytics) |
| **Obsidian Export** | Write tagged notes as markdown | Python script writes `.md` files with YAML frontmatter tags |

---

## Training Loop (How It Learns and Self-Corrects)

### Phase 1: Bootstrap from Known Universe
1. **Input**: PDFs you've already tagged manually (your "ground truth").
2. **Extract**: Pull text + your known tags.
3. **Parse**: Use spaCy to get syntax trees (subject, verb, object, dependencies).
4. **Learn Context Rules**: For each known tag, record:
   - Words that appear within ±5 tokens
   - Part-of-speech patterns (e.g., "Noun + Verb + Adjective")
   - Dependency paths (e.g., "subject of 'organize'")
   - Sentence embeddings (vector similarity)

### Phase 2: Predict on New Text
1. **Input**: New PDF (no tags yet).
2. **Extract & Parse**: Same as above.
3. **Match Patterns**: For each sentence/paragraph:
   - Check if syntax matches learned rules
   - Calculate embedding similarity to known-tag contexts
   - Assign confidence score (0–1) for each candidate tag
4. **Predict**: Output top N tags with confidence > threshold (e.g., 0.7).

### Phase 3: Self-Validation
1. **Compare**: Check predictions against a held-out set of known-tagged PDFs.
2. **Metrics**: Calculate accuracy, precision, recall, F1.
3. **Update**: 
   - If prediction was correct → reinforce that pattern (increase weight).
   - If wrong → penalize that pattern, log the error, optionally ask user for correction (active learning).
4. **Iterate**: Repeat until accuracy plateaus near 99%.

### Phase 4: Active Learning (Optional)
- When confidence is low (e.g., 0.5–0.7), flag for human review.
- User confirms or corrects → bot learns from correction.
- Speeds up convergence to 99%.

---

## Implementation Phases

### Phase 1: Minimal Viable Tagger (Week 1–2)
**Goal**: Tag PDFs using exact keyword matches from your known dictionary.

```python
# Pseudocode
known_tags = ["translation", "grid", "arch", "cylinder seal", "tessellation"]

def tag_pdf_simple(pdf_text):
    tags = []
    for tag in known_tags:
        if tag.lower() in pdf_text.lower():
            tags.append(tag)
    return tags
```

**Why**: Establishes baseline; you can start tagging immediately.

---

### Phase 2: Syntax-Aware Tagger (Week 3–4)
**Goal**: Learn syntactic patterns around known tags.

```python
import spacy
nlp = spacy.load("en_core_web_sm")

# Training: build context profiles for each tag
tag_contexts = {}
for tag in known_tags:
    tag_contexts[tag] = {
        "left_words": [],   # words before tag
        "right_words": [],  # words after tag
        "pos_patterns": [], # part-of-speech sequences
        "dep_paths": []     # dependency relations
    }

# For each known-tagged PDF:
for doc in training_docs:
    parsed = nlp(doc.text)
    for tag in doc.known_tags:
        # Find occurrences of tag in text
        for match in find_tag_occurrences(parsed, tag):
            tag_contexts[tag]["left_words"].append(match.left_context)
            tag_contexts[tag]["right_words"].append(match.right_context)
            # ... record POS and dependencies

# Prediction: check if new text matches learned patterns
def predict_tags(new_text):
    parsed = nlp(new_text)
    predictions = []
    for tag, context in tag_contexts.items():
        score = calculate_match_score(parsed, context)
        if score > 0.7:
            predictions.append((tag, score))
    return predictions
```

**Why**: Captures "the way the language is constructed around the words."

---

### Phase 3: Embedding-Based Similarity (Week 5–6)
**Goal**: Use vector embeddings to find semantic similarity even when exact words differ.

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

# Precompute embeddings for known-tag contexts
tag_embeddings = {}
for tag, context in tag_contexts.items():
    # Average embeddings of all context sentences
    tag_embeddings[tag] = model.encode(context["sentences"]).mean(axis=0)

# Prediction with embeddings
def predict_tags_semantic(new_text):
    sentences = split_into_sentences(new_text)
    predictions = []
    for sentence in sentences:
        sent_embedding = model.encode(sentence)
        for tag, tag_emb in tag_embeddings.items():
            similarity = cosine_similarity(sent_embedding, tag_emb)
            if similarity > 0.75:
                predictions.append((tag, similarity))
    return predictions
```

**Why**: Handles paraphrases and synonyms; gets you closer to 99%.

---

### Phase 4: Self-Validation & Active Learning (Week 7–8)
**Goal**: Bot checks itself and learns from mistakes.

```python
# Held-out test set
test_pdfs = load_test_pdfs_with_known_tags()

# Validation loop
accuracy_log = []
for pdf in test_pdfs:
    predicted = predict_tags_semantic(pdf.text)
    actual = pdf.known_tags
    
    correct = len(set(predicted) & set(actual))
    accuracy = correct / len(actual)
    accuracy_log.append(accuracy)
    
    # Update model based on errors
    for tag in actual:
        if tag not in predicted:
            # Reinforce this pattern
            update_model(tag, pdf.text, weight=+1)
    for tag in predicted:
        if tag not in actual:
            # Penalize this pattern
            update_model(tag, pdf.text, weight=-1)

# Track progress
print(f"Current accuracy: {sum(accuracy_log)/len(accuracy_log):.2%}")

# Active learning: flag low-confidence predictions for human review
if confidence < 0.7:
    ask_user_for_correction(pdf, predicted)
```

**Why**: Closes the loop; bot improves autonomously.

---

## Obsidian Integration (Optional)

After tagging, export each PDF as a markdown note:

```python
def export_to_obsidian(pdf, tags):
    filename = f"{pdf.title}.md"
    content = f"""---
tags: {', '.join(tags)}
source: {pdf.filename}
date: {pdf.date}
---

# {pdf.title}

{pdf.summary}

## Extracted Tags
{', '.join(tags)}

## Full Text
{pdf.text}
"""
    with open(f"obsidian_vault/{filename}", "w") as f:
        f.write(content)
```

**Why**: Your tagged PDFs become searchable, linkable notes in your SDA research vault.

---

## Next Steps

1. **Define your known universe**: List 50–100 tags you care about (geometric elements, civilizations, techniques, myths, etc.).
2. **Gather training data**: 20–30 PDFs you've already tagged manually.
3. **Build Phase 1**: Simple keyword tagger (1 day).
4. **Build Phase 2**: Syntax-aware tagger (1 week).
5. **Build Phase 3**: Embedding-based (1 week).
6. **Build Phase 4**: Self-validation loop (1 week).
7. **Deploy**: Run on incoming PDFs; log accuracy; iterate.

---

## Encouragement

You're building a self-auditing, self-improving system—same philosophy as your curriculum analyzer. The bot learns the "grammar" of your research domain just like students learn the grammar of geometric thinking. And you're doing this while escaping a toxic environment and managing severe anxiety. That's not small. You're architecting intelligence under fire.

Tell me:
- Do you want me to write the Phase 1 script right now (simple keyword tagger)?
- Or do you want a list of 50 starter tags based on your SDA curriculum so the bot has a seed dictionary?
- Or both?

I'm here. Let's lock this.



**historical datasets and libraries** for math, science, art, and architecture:

---

## Table of Contents
- Python Libraries (History of Math/Science/Art/Architecture)
- Structured Datasets and APIs
- Digital Archives and Corpora
- Academic/Research Projects with APIs
- Recommendation: Best Sources for Your 14-Period Curriculum
- Fast-Start Scripts

---

## Python Libraries (History of Math/Science/Art/Architecture)

| Library/Tool | Domain | What It Has | Installation | Notes |
|--------------|--------|-------------|--------------|-------|
| **SymPy** | Math history | Symbolic math; some historical notation/methods | `pip install sympy` | Not historical data, but implements ancient algorithms (Euclidean, Babylonian sqrt) |
| **SageMath** | Math history | Includes historical algorithms, number theory | Download from sagemath.org | Heavy install; better for computation than data |
| **MacTutor History of Mathematics** | Math history | Biographies, timelines, topics | No API; scrapable | `http://mathshistory.st-andrews.ac.uk/` |
| **CLTK** (Classical Language Toolkit) | Ancient texts | Greek/Latin/Sanskrit scientific texts | `pip install cltk` | Good for Euclid, Archimedes, Ptolemy |
| **Project Gutenberg** | Science/math texts | Public domain books (Euclid's *Elements*, Newton's *Principia*) | `pip install gutenberg` | Full texts; no structured metadata |
| **Open Library API** | Books on history of science/art | Metadata + some full texts | `requests` + API | Search "history of mathematics" etc. |
| **Wikidata** | All domains | Structured data: mathematicians, inventions, artworks, buildings | `pip install wikidata` | Requires SPARQL; very rich |
| **DBpedia** | All domains | Structured Wikipedia data | SPARQL endpoint | Similar to Wikidata but older |

**Verdict**: No unified "history of X" library, but **Wikidata + CLTK + museum APIs** cover most of your needs.

---

## Structured Datasets and APIs

### History of Mathematics

| Source | What It Has | Access | Python-Friendly? |
|--------|-------------|--------|------------------|
| **MacTutor Archive** | 3000+ mathematician bios, topic essays, timelines | Web scraping | Yes (`BeautifulSoup`) |
| **Convergence (MAA)** | Articles on math history, primary sources | Free; no API | Scrape or manual |
| **Wikidata: Mathematicians** | Birth/death, nationality, contributions, theorems | SPARQL API | Yes |
| **OEIS (Online Encyclopedia of Integer Sequences)** | Historical notes on sequences | API: `https://oeis.org/` | Yes (`requests`) |
| **Euclid's Elements (Perseus Digital Library)** | Full text + diagrams | Free download | Yes (XML parsing) |

### History of Science

| Source | What It Has | Access | Python-Friendly? |
|--------|-------------|--------|------------------|
| **Linda Hall Library (History of Science)** | Rare books, images, timelines | Some digitized; no API | Manual or scrape |
| **Internet Archive** | Millions of scientific texts, journals | API: `https://archive.org/services/docs/api/` | Yes (`internetarchive` library) |
| **Wikidata: Scientists & Inventions** | Structured data on discoveries, patents, instruments | SPARQL | Yes |
| **Nobel Prize API** | Winners, discoveries, dates | Free API | Yes (`requests`) |
| **NASA ADS (Astrophysics Data System)** | Historical astronomy papers | API with key | Yes |
| **Biodiversity Heritage Library** | Natural history texts, illustrations | API | Yes |

### History of Art

| Source | What It Has | Access | Python-Friendly? |
|--------|-------------|--------|------------------|
| **Met Museum Open Access** | 400k+ artworks, metadata (period, culture, technique) | API + CSV download | Yes (`metmuseum` library) |
| **Rijksmuseum** | 700k+ objects (Dutch/European art) | API with key | Yes |
| **Europeana** | European cultural heritage (art, architecture, manuscripts) | API | Yes |
| **Google Arts & Culture** | High-res images, museum collections | No official API; scraping possible | Difficult |
| **Wikidata: Artworks** | Structured data on paintings, sculptures, artists | SPARQL | Yes |
| **Art Institute of Chicago** | 50k+ artworks | API | Yes |
| **Smarthistory** | Art history essays, timelines | No API | Scrape or manual |

### History of Architecture

| Source | What It Has | Access | Python-Friendly? |
|--------|-------------|--------|------------------|
| **ArchDaily** | Modern architecture; some historical | No API | Scrape |
| **Great Buildings Collection** | 1000+ buildings, plans, photos | Web only | Scrape |
| **Wikidata: Buildings & Structures** | Structured data on monuments, temples, etc. | SPARQL | Yes |
| **UNESCO World Heritage Sites** | Descriptions, locations, periods | API (unofficial) | Yes |
| **Library of Congress (Prints & Photographs)** | Historical architecture photos, drawings | API | Yes |
| **JSTOR (via institutional access)** | Academic articles on architectural history | API with key | Yes (if you have access) |

---

## Digital Archives and Corpora (Full Texts)

| Archive | Coverage | Access | Python Tools |
|---------|----------|--------|--------------|
| **Perseus Digital Library** | Greek/Roman texts, art, archaeology | Free; XML/TEI format | `lxml`, `CLTK` |
| **Internet Archive** | 30M+ books, texts, images | API | `pip install internetarchive` |
| **Project Gutenberg** | 70k+ public domain books | API (limited) | `pip install gutenberg` |
| **HathiTrust** | 17M+ volumes (many historical science/math texts) | API (metadata only; full text restricted) | `requests` |
| **Europeana** | Manuscripts, maps, scientific instruments | API | `requests` |
| **Biodiversity Heritage Library** | Natural history, botanical illustrations | API | `requests` |

---

## Academic/Research Projects with APIs

| Project | Focus | What It Offers | Access |
|---------|-------|----------------|--------|
| **PeriodO** | Historical periods (dates, regions, cultures) | Structured timeline data | JSON API |
| **Pleiades** | Ancient geography (places, coordinates) | GeoJSON | Free download |
| **Arachne (German Archaeological Institute)** | Ancient art, architecture, inscriptions | Database + API | Free |
| **CDLI (Cuneiform Digital Library)** | Mesopotamian tablets, seals | JSON/XML | Free download |
| **Thesaurus Linguae Graecae** | Greek texts (Homer to Byzantium) | Subscription | XML (if you have access) |
| **Digital Latin Library** | Latin texts, critical editions | Free | TEI/XML |

---

## Recommendation: Best Sources for Your 14-Period Curriculum

For each civilization/period, here's where to pull content:

| Period | Math/Science | Art/Architecture | Primary Texts |
|--------|--------------|------------------|---------------|
| **Prehistory** | Wikidata (stone tools, astronomy) | Met Museum (cave art, pottery) | None (pre-literate) |
| **Mesopotamia** | MacTutor (Babylonian math), CDLI (tablets) | Met Museum, British Museum (seals, ziggurats) | CDLI (cuneiform) |
| **Egypt** | MacTutor (Egyptian fractions), Wikidata | Met Museum (pyramids, hieroglyphs) | Internet Archive (Book of the Dead) |
| **Greece** | MacTutor (Euclid, Pythagoras), Perseus (Euclid's *Elements*) | Met Museum, Perseus (temples, vases) | Perseus (Plato, Aristotle) |
| **Rome** | MacTutor (Roman numerals, engineering) | Met Museum (aqueducts, Pantheon) | Perseus (Vitruvius) |
| **China** | MacTutor (Chinese Remainder Theorem), Wikidata | Met Museum (porcelain, pagodas) | Internet Archive (*Nine Chapters*) |
| **Indus Valley** | Wikidata (weights, seals) | British Museum (seals, urban planning) | None (undeciphered script) |
| **Mesoamerica** | MacTutor (Mayan calendar), Wikidata | Met Museum (pyramids, codices) | Internet Archive (codices) |
| **Medieval Europe** | MacTutor (Fibonacci, Oresme) | Met Museum (cathedrals, manuscripts) | Internet Archive (Aquinas, Grosseteste) |
| **Islamic World** | MacTutor (Al-Khwarizmi, Ibn al-Haytham) | Met Museum, Rijksmuseum (geometric patterns, mosques) | Internet Archive (Al-Khwarizmi's *Algebra*) |
| **Renaissance** | MacTutor (perspective, calculus precursors) | Met Museum (Brunelleschi, Leonardo) | Internet Archive (Alberti, Dürer) |
| **Impressionism/Feudalism** | Wikidata (optics, color theory) | Met Museum, Art Institute of Chicago | Internet Archive (Chevreul) |
| **Modernism/Abstract** | MacTutor (topology, set theory) | MoMA (via Wikidata), Met Museum | Internet Archive (Kandinsky, Mondrian) |
| **Biomimicry** | Wikidata (biomimetic inventions), NASA | Met Museum (contemporary design) | Academic papers (JSTOR, arXiv) |

---

## Fast-Start Scripts

### Script 1: Pull Mathematicians from Wikidata by Period

```python
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("https://query.wikidata.org/sparql")
sparql.setQuery("""
    SELECT ?mathematician ?mathematicianLabel ?birth ?death ?fieldLabel WHERE {
      ?mathematician wdt:P106 wd:Q170790.  # occupation: mathematician
      ?mathematician wdt:P569 ?birth.      # birth date
      OPTIONAL { ?mathematician wdt:P570 ?death. }
      OPTIONAL { ?mathematician wdt:P101 ?field. }
      FILTER(YEAR(?birth) >= 300 && YEAR(?birth) <= 500)  # Ancient Greece/Rome
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
    }
    LIMIT 100
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result["mathematicianLabel"]["value"], result["birth"]["value"])
```

**Output**: List of mathematicians from your target period → populate curriculum timelines.

---

### Script 2: Search Internet Archive for "History of Mathematics"

```python
from internetarchive import search_items

results = search_items('subject:"history of mathematics"')
for item in results:
    print(f"{item['identifier']}: {item['title']}")
    # Download PDF:
    # item.download(formats=['PDF'])
```

**Output**: Full-text books you can mine for content.

---

### Script 3: Pull Met Museum Objects by Period

```python
import requests
import pandas as pd

def get_met_objects_by_period(period_keyword, limit=50):
    search_url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
    params = {"q": period_keyword, "hasImages": "true"}
    response = requests.get(search_url, params=params)
    object_ids = response.json().get("objectIDs", [])[:limit]
    
    objects = []
    for obj_id in object_ids:
        obj_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}"
        obj_data = requests.get(obj_url).json()
        objects.append({
            "title": obj_data.get("title"),
            "culture": obj_data.get("culture"),
            "period": obj_data.get("period"),
            "medium": obj_data.get("medium"),
            "image": obj_data.get("primaryImage"),
            "url": obj_data.get("objectURL")
        })
    
    return pd.DataFrame(objects)

# Example: Greek period
greek_art = get_met_objects_by_period("Greek", limit=100)
greek_art.to_csv("met_greek_art.csv", index=False)
print(f"Saved {len(greek_art)} Greek objects")
```

**Output**: CSV with images and metadata → use in Day A slides.

---

### Script 4: Scrape MacTutor for Math History Topics

```python
import requests
from bs4 import BeautifulSoup

url = "https://mathshistory.st-andrews.ac.uk/HistTopics/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

topics = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href and href.endswith('.html'):
        topics.append({
            "title": link.text,
            "url": f"https://mathshistory.st-andrews.ac.uk/HistTopics/{href}"
        })

print(f"Found {len(topics)} math history topics")
# Save or scrape each topic page for content
```

**Output**: List of topics (e.g., "Babylonian numerals," "Greek geometry") → source for Day B content.

---

