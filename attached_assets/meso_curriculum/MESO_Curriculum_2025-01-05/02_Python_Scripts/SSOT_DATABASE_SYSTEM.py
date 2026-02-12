#!/usr/bin/env python3
"""
MESO CURRICULUM - SSOT DATABASE SYSTEM
Single Source of Truth linking everything together:
SSOTs → eTextbooks → Chapters → Lessons → Content → Assets → Specifications
"""

import sqlite3
import json
from pathlib import Path
from datetime import datetime

class SSOTDatabase:
    def __init__(self, db_path="meso_ssot_complete.db"):
        self.db_path = db_path
        self.conn = None
        
    def connect(self):
        """Connect to database"""
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON")
        return self.conn
        
    def create_complete_schema(self):
        """Create comprehensive SSOT schema"""
        cursor = self.conn.cursor()
        
        # ================================================================
        # LEVEL 1: SSOT (Single Source of Truth)
        # ================================================================
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ssots (
                ssot_id TEXT PRIMARY KEY,
                ssot_type TEXT NOT NULL,
                title TEXT NOT NULL,
                description TEXT,
                grade_level INTEGER,
                subject TEXT,
                version TEXT DEFAULT '1.0',
                status TEXT DEFAULT 'DRAFT',
                author TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                published_at TIMESTAMP,
                file_path TEXT,
                master_template TEXT,
                CHECK (ssot_type IN ('CURRICULUM', 'ETEXTBOOK', 'LESSON', 'UNIT', 'MODULE'))
            )
        """)
        
        # ================================================================
        # LEVEL 2: ETEXTBOOKS (Collection of Chapters)
        # ================================================================
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS etextbooks (
                etextbook_id TEXT PRIMARY KEY,
                ssot_id TEXT NOT NULL,
                title TEXT NOT NULL,
                subtitle TEXT,
                grade_level INTEGER NOT NULL,
                isbn TEXT,
                page_count INTEGER,
                format TEXT DEFAULT 'PDF',
                version TEXT DEFAULT '1.0',
                status TEXT DEFAULT 'DRAFT',
                cover_image TEXT,
                toc_json TEXT,
                standards_covered TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (ssot_id) REFERENCES ssots(ssot_id)
            )
        """)
        
        # ================================================================
        # LEVEL 3: CHAPTERS (Sections within eTextbooks)
        # ================================================================
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chapters (
                chapter_id TEXT PRIMARY KEY,
                etextbook_id TEXT NOT NULL,
                chapter_number INTEGER NOT NULL,
                title TEXT NOT NULL,
                subtitle TEXT,
                page_start INTEGER,
                page_end INTEGER,
                duration_minutes INTEGER,
                learning_objectives TEXT,
                key_vocabulary TEXT,
                standards TEXT,
                chapter_type TEXT,
                content_summary TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (etextbook_id) REFERENCES etextbooks(etextbook_id),
                UNIQUE(etextbook_id, chapter_number),
                CHECK (chapter_type IN ('INTRO', 'MYTH', 'GEOMETRY', 'ACTIVITY', 'ASSESSMENT', 'REFLECTION'))
            )
        """)
        
        # ================================================================
        # LEVEL 4: LESSONS (Teaching Units)
        # ================================================================
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lessons (
                lesson_id TEXT PRIMARY KEY,
                chapter_id TEXT,
                ssot_id TEXT,
                lesson_key TEXT UNIQUE NOT NULL,
                lesson_name TEXT NOT NULL,
                grade INTEGER NOT NULL,
                week INTEGER,
                lesson_letter TEXT,
                deity_name TEXT,
                geometric_concept TEXT,
                math_standard TEXT,
                artifact_type TEXT,
                measurement_focus TEXT,
                myth_theme TEXT,
                activity_medium TEXT,
                canva_color_scheme TEXT,
                duration_minutes INTEGER DEFAULT 50,
                standards TEXT,
                compliance_tags TEXT,
                estimated_images INTEGER,
                lesson_structure TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (chapter_id) REFERENCES chapters(chapter_id),
                FOREIGN KEY (ssot_id) REFERENCES ssots(ssot_id)
            )
        """)
        
        # ================================================================
        # LEVEL 5: CONTENT BLOCKS (Granular Content)
        # ================================================================
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS content_blocks (
                content_id INTEGER PRIMARY KEY AUTOINCREMENT,
                lesson_id TEXT NOT NULL,
                chapter_id TEXT,
                block_type TEXT NOT NULL,
                block_order INTEGER NOT NULL,
                section_name TEXT,
                title TEXT,
                body_text TEXT,
                instructions TEXT,
                duration_seconds INTEGER,
                interactivity_level TEXT,
                accessibility_notes TEXT,
                metadata_json TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id),
                FOREIGN KEY (chapter_id) REFERENCES chapters(chapter_id),
                CHECK (block_type IN ('TEXT', 'MYTH', 'IMAGE', 'VIDEO', 'ACTIVITY', 'QUESTION', 'DIAGRAM', 'WORKSHEET'))
            )
        """)
        
        # ================================================================
        # LEVEL 6: ASSETS (All Media)
        # ================================================================
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS assets (
                asset_id TEXT PRIMARY KEY,
                lesson_id TEXT,
                chapter_id TEXT,
                content_id INTEGER,
                asset_type TEXT NOT NULL,
                subtype TEXT,
                code TEXT,
                version INTEGER DEFAULT 1,
                status TEXT DEFAULT 'DRAFT',
                filename TEXT NOT NULL,
                filepath TEXT,
                usage_role TEXT NOT NULL,
                format TEXT NOT NULL,
                width_px INTEGER,
                height_px INTEGER,
                duration_seconds REAL,
                file_size_kb INTEGER,
                alt_text TEXT,
                caption TEXT,
                license TEXT DEFAULT 'CC BY 4.0',
                credit TEXT,
                created_with TEXT,
                source_ref TEXT,
                notes_internal TEXT,
                tags TEXT,
                checksum TEXT,
                parent_asset_id TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id),
                FOREIGN KEY (chapter_id) REFERENCES chapters(chapter_id),
                FOREIGN KEY (content_id) REFERENCES content_blocks(content_id),
                FOREIGN KEY (parent_asset_id) REFERENCES assets(asset_id),
                CHECK (asset_type IN ('IMG', 'VID', 'AUD', 'DOC', 'OVL', 'DATA'))
            )
        """)
        
        # ================================================================
        # LEVEL 7: SPECIFICATIONS (Technical Requirements)
        # ================================================================
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS specifications (
                spec_id INTEGER PRIMARY KEY AUTOINCREMENT,
                asset_id TEXT NOT NULL,
                spec_type TEXT NOT NULL,
                spec_category TEXT,
                spec_name TEXT NOT NULL,
                spec_value TEXT NOT NULL,
                required BOOLEAN DEFAULT 1,
                priority TEXT DEFAULT 'MEDIUM',
                validation_rule TEXT,
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (asset_id) REFERENCES assets(asset_id),
                CHECK (spec_type IN ('DIMENSION', 'FORMAT', 'COLOR', 'FONT', 'QUALITY', 'ACCESSIBILITY', 'TECHNICAL', 'EXPORT')),
                CHECK (priority IN ('LOW', 'MEDIUM', 'HIGH', 'CRITICAL'))
            )
        """)
        
        # ================================================================
        # SUPPORTING TABLES
        # ================================================================
        
        # Sections (within Lessons)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sections (
                section_id INTEGER PRIMARY KEY AUTOINCREMENT,
                lesson_id TEXT NOT NULL,
                section_number INTEGER NOT NULL,
                section_name TEXT NOT NULL,
                duration_minutes INTEGER,
                slide_range TEXT,
                content_type TEXT,
                FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id),
                UNIQUE(lesson_id, section_number)
            )
        """)
        
        # Slides (Presentation Elements)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS slides (
                slide_id INTEGER PRIMARY KEY AUTOINCREMENT,
                lesson_id TEXT NOT NULL,
                section_id INTEGER,
                slide_number INTEGER NOT NULL,
                slide_title TEXT,
                slide_content TEXT,
                speaker_notes TEXT,
                asset_ids TEXT,
                duration_seconds INTEGER,
                layout_type TEXT,
                FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id),
                FOREIGN KEY (section_id) REFERENCES sections(section_id),
                UNIQUE(lesson_id, slide_number)
            )
        """)
        
        # Overlays (Geometric/Annotation)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS overlays (
                overlay_id INTEGER PRIMARY KEY AUTOINCREMENT,
                lesson_id TEXT NOT NULL,
                asset_id TEXT,
                category TEXT NOT NULL,
                overlay_code TEXT NOT NULL,
                description TEXT,
                svg_path TEXT,
                color_hex TEXT,
                line_weight INTEGER,
                opacity REAL DEFAULT 1.0,
                animation_type TEXT,
                FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id),
                FOREIGN KEY (asset_id) REFERENCES assets(asset_id)
            )
        """)
        
        # Standards (Educational Standards)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS standards (
                standard_id INTEGER PRIMARY KEY AUTOINCREMENT,
                standard_code TEXT UNIQUE NOT NULL,
                grade_level INTEGER,
                domain TEXT,
                cluster TEXT,
                description TEXT,
                full_text TEXT
            )
        """)
        
        # Lesson-Standard Junction
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS lesson_standards (
                lesson_id TEXT NOT NULL,
                standard_id INTEGER NOT NULL,
                alignment_strength TEXT DEFAULT 'FULL',
                notes TEXT,
                FOREIGN KEY (lesson_id) REFERENCES lessons(lesson_id),
                FOREIGN KEY (standard_id) REFERENCES standards(standard_id),
                PRIMARY KEY (lesson_id, standard_id),
                CHECK (alignment_strength IN ('FULL', 'PARTIAL', 'SUPPORTING'))
            )
        """)
        
        # Tags (Controlled Vocabulary)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tags (
                tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
                tag_name TEXT UNIQUE NOT NULL,
                tag_category TEXT NOT NULL,
                description TEXT
            )
        """)
        
        # Asset-Tag Junction
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS asset_tags (
                asset_id TEXT NOT NULL,
                tag_id INTEGER NOT NULL,
                relevance REAL DEFAULT 1.0,
                FOREIGN KEY (asset_id) REFERENCES assets(asset_id),
                FOREIGN KEY (tag_id) REFERENCES tags(tag_id),
                PRIMARY KEY (asset_id, tag_id)
            )
        """)
        
        # Dependencies (Asset/Content Dependencies)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS dependencies (
                dependency_id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_type TEXT NOT NULL,
                source_id TEXT NOT NULL,
                target_type TEXT NOT NULL,
                target_id TEXT NOT NULL,
                dependency_type TEXT NOT NULL,
                required BOOLEAN DEFAULT 1,
                notes TEXT,
                CHECK (source_type IN ('SSOT', 'ETEXTBOOK', 'CHAPTER', 'LESSON', 'CONTENT', 'ASSET')),
                CHECK (target_type IN ('SSOT', 'ETEXTBOOK', 'CHAPTER', 'LESSON', 'CONTENT', 'ASSET')),
                CHECK (dependency_type IN ('REQUIRES', 'REFERENCES', 'DERIVES_FROM', 'INCLUDES', 'PRECEDES'))
            )
        """)
        
        # Production Status Tracking
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS production_status (
                status_id INTEGER PRIMARY KEY AUTOINCREMENT,
                entity_type TEXT NOT NULL,
                entity_id TEXT NOT NULL,
                stage TEXT NOT NULL,
                status TEXT NOT NULL,
                assigned_to TEXT,
                due_date TIMESTAMP,
                completed_at TIMESTAMP,
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                CHECK (entity_type IN ('SSOT', 'ETEXTBOOK', 'CHAPTER', 'LESSON', 'ASSET')),
                CHECK (stage IN ('PLANNING', 'DRAFTING', 'REVIEW', 'REVISION', 'APPROVAL', 'PRODUCTION', 'QA', 'PUBLISHED')),
                CHECK (status IN ('NOT_STARTED', 'IN_PROGRESS', 'BLOCKED', 'COMPLETED', 'NEEDS_REVIEW'))
            )
        """)
        
        self.conn.commit()
        print("✅ Complete SSOT database schema created")
        
    def seed_sample_data(self):
        """Seed with Grade 3 curriculum data"""
        cursor = self.conn.cursor()
        
        # LEVEL 1: SSOT
        cursor.execute("""
            INSERT OR IGNORE INTO ssots (ssot_id, ssot_type, title, description, grade_level, subject, version, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            'SSOT-MESO-G3',
            'CURRICULUM',
            'MESO Grade 3 Curriculum',
            'Mesopotamian geometry curriculum for Grade 3',
            3,
            'Mathematics/Geometry',
            '2.0',
            'ACTIVE'
        ))
        
        # LEVEL 2: ETEXTBOOK
        cursor.execute("""
            INSERT OR IGNORE INTO etextbooks (etextbook_id, ssot_id, title, subtitle, grade_level, page_count, format, version, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            'EBOOK-G3-CIRCLES',
            'SSOT-MESO-G3',
            'Circles in Mesopotamian Geometry',
            'Grade 3 eTextbook - Unit 1',
            3,
            150,
            'PDF',
            '1.0',
            'DRAFT'
        ))
        
        # LEVEL 3: CHAPTERS
        chapters_data = [
            ('CHAP-G3-01A', 'EBOOK-G3-CIRCLES', 1, 'Shamash & The Circle', 'Divine perfection through circles', 1, 20, 50, 'MYTH'),
            ('CHAP-G3-01B', 'EBOOK-G3-CIRCLES', 2, 'The Sun & Circle of Sharing', 'Fairness through partitioning', 21, 40, 50, 'GEOMETRY')
        ]
        
        for chapter in chapters_data:
            cursor.execute("""
                INSERT OR IGNORE INTO chapters (chapter_id, etextbook_id, chapter_number, title, subtitle, page_start, page_end, duration_minutes, chapter_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, chapter)
        
        # LEVEL 4: LESSONS
        lessons_data = [
            {
                'lesson_id': 'G3-1A',
                'chapter_id': 'CHAP-G3-01A',
                'ssot_id': 'SSOT-MESO-G3',
                'lesson_key': 'meso_G3_1A',
                'lesson_name': 'Shamash & The Circle',
                'grade': 3,
                'week': 1,
                'lesson_letter': 'A',
                'deity_name': 'Shamash',
                'geometric_concept': 'Circles, radius, diameter',
                'math_standard': 'Perimeter and area',
                'artifact_type': 'Sun disc seals',
                'measurement_focus': 'Radius, diameter, circumference',
                'myth_theme': 'Divine perfection',
                'activity_medium': 'Compass drawing',
                'canva_color_scheme': 'Gold #FFD24A, Orange',
                'duration_minutes': 50,
                'standards': '3.MD.C.5, 3.MD.C.6, 3.G.A.1',
                'estimated_images': 48
            },
            {
                'lesson_id': 'G3-1B',
                'chapter_id': 'CHAP-G3-01B',
                'ssot_id': 'SSOT-MESO-G3',
                'lesson_key': 'meso_G3_1B',
                'lesson_name': 'The Sun & Circle of Sharing',
                'grade': 3,
                'week': 1,
                'lesson_letter': 'B',
                'deity_name': 'Sun (generic)',
                'geometric_concept': 'Circles, halves, fourths',
                'math_standard': 'Partition shapes',
                'artifact_type': 'Sun disc motifs',
                'measurement_focus': 'Equal parts, center',
                'myth_theme': 'Fairness through geometry',
                'activity_medium': 'Paper folding, spinner',
                'canva_color_scheme': 'Sky Gold #FFD24A, River Blue #2B6CB0',
                'duration_minutes': 50,
                'standards': '3.G.A.1, 3.G.A.2, 3.G.A.3',
                'estimated_images': 48
            }
        ]
        
        for lesson in lessons_data:
            cursor.execute("""
                INSERT OR IGNORE INTO lessons (
                    lesson_id, chapter_id, ssot_id, lesson_key, lesson_name, grade, week, lesson_letter,
                    deity_name, geometric_concept, math_standard, artifact_type, measurement_focus,
                    myth_theme, activity_medium, canva_color_scheme, duration_minutes, standards, estimated_images
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                lesson['lesson_id'], lesson['chapter_id'], lesson['ssot_id'], lesson['lesson_key'],
                lesson['lesson_name'], lesson['grade'], lesson['week'], lesson['lesson_letter'],
                lesson['deity_name'], lesson['geometric_concept'], lesson['math_standard'],
                lesson['artifact_type'], lesson['measurement_focus'], lesson['myth_theme'],
                lesson['activity_medium'], lesson['canva_color_scheme'], lesson['duration_minutes'],
                lesson['standards'], lesson['estimated_images']
            ))
        
        # LEVEL 5: CONTENT BLOCKS (Sample for G3-1B)
        content_blocks = [
            ('G3-1B', 'CHAP-G3-01B', 'TEXT', 1, 'Look and Wonder', 'Opening Questions', 'What is round in these pictures? How can a circle help us share?', None, 120, 'LOW', 'Images with alt text'),
            ('G3-1B', 'CHAP-G3-01B', 'MYTH', 2, 'The Myth', 'Sun & Sharing Story', 'The sun wakes over the river...', 'Read aloud with visual supports', 180, 'MEDIUM', 'Full myth text with overlays'),
            ('G3-1B', 'CHAP-G3-01B', 'DIAGRAM', 3, 'Geometry', 'Circle Parts', 'Find center, make halves, make fourths', 'Demonstrate with overlay', 300, 'HIGH', 'Interactive overlays'),
            ('G3-1B', 'CHAP-G3-01B', 'ACTIVITY', 4, 'Circle Collage', 'Art Activity', 'Tear paper, glue into halves/fourths', 'Step-by-step instructions', 600, 'HIGH', 'Materials list provided'),
            ('G3-1B', 'CHAP-G3-01B', 'WORKSHEET', 5, 'Practice', 'Student Worksheet', 'Draw circles, partition into equal parts', 'Independent practice', 480, 'MEDIUM', 'Printable PDF')
        ]
        
        for block in content_blocks:
            cursor.execute("""
                INSERT INTO content_blocks (lesson_id, chapter_id, block_type, block_order, section_name, title, body_text, instructions, duration_seconds, interactivity_level, accessibility_notes)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, block)
        
        # LEVEL 6: ASSETS (Sample for G3-1B)
        assets_data = [
            {
                'asset_id': 'meso_G3_1B-IMG-ILL_myth_01_sun_river',
                'lesson_id': 'G3-1B',
                'chapter_id': 'CHAP-G3-01B',
                'asset_type': 'IMG',
                'subtype': 'ILL',
                'filename': 'meso_G3_1B-IMG-ILL_myth_01_sun_river.png',
                'usage_role': 'myth',
                'format': 'PNG',
                'width_px': 3840,
                'height_px': 2160,
                'alt_text': 'A bright round sun rises over a blue river at dawn.',
                'caption': 'The sun wakes over the river with steady cycles.'
            },
            {
                'asset_id': 'meso_G3_1B-OVL-center_CENTER_Dot',
                'lesson_id': 'G3-1B',
                'chapter_id': 'CHAP-G3-01B',
                'asset_type': 'OVL',
                'subtype': 'center',
                'code': 'CENTER_Dot',
                'filename': 'meso_G3_1B-OVL-center_CENTER_Dot.svg',
                'usage_role': 'overlay',
                'format': 'SVG',
                'alt_text': 'Center point indicator with pulse animation.'
            }
        ]
        
        for asset in assets_data:
            cursor.execute("""
                INSERT OR IGNORE INTO assets (
                    asset_id, lesson_id, chapter_id, asset_type, subtype, code, filename,
                    usage_role, format, width_px, height_px, alt_text, caption
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                asset['asset_id'], asset['lesson_id'], asset['chapter_id'], asset['asset_type'],
                asset.get('subtype'), asset.get('code'), asset['filename'], asset['usage_role'],
                asset['format'], asset.get('width_px'), asset.get('height_px'),
                asset['alt_text'], asset.get('caption')
            ))
        
        # LEVEL 7: SPECIFICATIONS (Sample)
        specs_data = [
            ('meso_G3_1B-IMG-ILL_myth_01_sun_river', 'DIMENSION', 'SIZE', 'Width', '3840', True, 'CRITICAL', 'width_px >= 3840'),
            ('meso_G3_1B-IMG-ILL_myth_01_sun_river', 'DIMENSION', 'SIZE', 'Height', '2160', True, 'CRITICAL', 'height_px >= 2160'),
            ('meso_G3_1B-IMG-ILL_myth_01_sun_river', 'FORMAT', 'FILE', 'Format', 'PNG', True, 'HIGH', 'format == PNG'),
            ('meso_G3_1B-IMG-ILL_myth_01_sun_river', 'COLOR', 'PALETTE', 'Color Space', 'sRGB', True, 'MEDIUM', 'color_space == sRGB'),
            ('meso_G3_1B-IMG-ILL_myth_01_sun_river', 'QUALITY', 'RESOLUTION', 'DPI', '300', True, 'HIGH', 'dpi >= 300'),
            ('meso_G3_1B-IMG-ILL_myth_01_sun_river', 'ACCESSIBILITY', 'TEXT', 'Alt Text Length', '80-140', True, 'CRITICAL', 'len(alt_text) BETWEEN 80 AND 140'),
            ('meso_G3_1B-OVL-center_CENTER_Dot', 'FORMAT', 'FILE', 'Format', 'SVG', True, 'CRITICAL', 'format == SVG'),
            ('meso_G3_1B-OVL-center_CENTER_Dot', 'TECHNICAL', 'VECTOR', 'Scalable', 'true', True, 'HIGH', 'is_vector == true')
        ]
        
        for spec in specs_data:
            cursor.execute("""
                INSERT INTO specifications (asset_id, spec_type, spec_category, spec_name, spec_value, required, priority, validation_rule)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, spec)
        
        # Dependencies
        cursor.execute("""
            INSERT INTO dependencies (source_type, source_id, target_type, target_id, dependency_type, required)
            VALUES 
                ('ETEXTBOOK', 'EBOOK-G3-CIRCLES', 'SSOT', 'SSOT-MESO-G3', 'DERIVES_FROM', 1),
                ('CHAPTER', 'CHAP-G3-01B', 'ETEXTBOOK', 'EBOOK-G3-CIRCLES', 'REQUIRES', 1),
                ('LESSON', 'G3-1B', 'CHAPTER', 'CHAP-G3-01B', 'REQUIRES', 1),
                ('ASSET', 'meso_G3_1B-IMG-ILL_myth_01_sun_river', 'LESSON', 'G3-1B', 'REQUIRES', 1),
                ('ASSET', 'meso_G3_1B-OVL-center_CENTER_Dot', 'LESSON', 'G3-1B', 'REQUIRES', 1)
        """)
        
        self.conn.commit()
        print("✅ Sample data seeded")
        
    def query_full_hierarchy(self, lesson_id):
        """Query complete hierarchy for a lesson"""
        cursor = self.conn.cursor()
        
        # Get full hierarchy
        cursor.execute("""
            SELECT 
                s.ssot_id, s.title as ssot_title,
                e.etextbook_id, e.title as etextbook_title,
                c.chapter_id, c.title as chapter_title,
                l.lesson_id, l.lesson_name,
                COUNT(DISTINCT cb.content_id) as content_blocks,
                COUNT(DISTINCT a.asset_id) as assets,
                COUNT(DISTINCT sp.spec_id) as specifications
            FROM lessons l
            LEFT JOIN chapters c ON l.chapter_id = c.chapter_id
            LEFT JOIN etextbooks e ON c.etextbook_id = e.etextbook_id
            LEFT JOIN ssots s ON e.ssot_id = s.ssot_id
            LEFT JOIN content_blocks cb ON l.lesson_id = cb.lesson_id
            LEFT JOIN assets a ON l.lesson_id = a.lesson_id
            LEFT JOIN specifications sp ON a.asset_id = sp.asset_id
            WHERE l.lesson_id = ?
            GROUP BY l.lesson_id
        """, (lesson_id,))
        
        result = cursor.fetchone()
        if result:
            return dict(result)
        return None
        
    def export_complete_manifest(self, lesson_id, output_path):
        """Export complete manifest with all linked data"""
        cursor = self.conn.cursor()
        
        # Get lesson
        cursor.execute("SELECT * FROM lessons WHERE lesson_id = ?", (lesson_id,))
        lesson = dict(cursor.fetchone())
        
        # Get chapter
        cursor.execute("SELECT * FROM chapters WHERE chapter_id = ?", (lesson['chapter_id'],))
        chapter = dict(cursor.fetchone())
        
        # Get etextbook
        cursor.execute("SELECT * FROM etextbooks WHERE etextbook_id = ?", (chapter['etextbook_id'],))
        etextbook = dict(cursor.fetchone())
        
        # Get SSOT
        cursor.execute("SELECT * FROM ssots WHERE ssot_id = ?", (etextbook['ssot_id'],))
        ssot = dict(cursor.fetchone())
        
        # Get content blocks
        cursor.execute("SELECT * FROM content_blocks WHERE lesson_id = ?", (lesson_id,))
        content_blocks = [dict(row) for row in cursor.fetchall()]
        
        # Get assets with specs
        cursor.execute("""
            SELECT a.*, GROUP_CONCAT(s.spec_name || ': ' || s.spec_value) as specifications
            FROM assets a
            LEFT JOIN specifications s ON a.asset_id = s.asset_id
            WHERE a.lesson_id = ?
            GROUP BY a.asset_id
        """, (lesson_id,))
        assets = [dict(row) for row in cursor.fetchall()]
        
        # Get dependencies
        cursor.execute("""
            SELECT * FROM dependencies 
            WHERE (source_type = 'LESSON' AND source_id = ?)
               OR (target_type = 'LESSON' AND target_id = ?)
        """, (lesson_id, lesson_id))
        dependencies = [dict(row) for row in cursor.fetchall()]
        
        manifest = {
            'ssot': ssot,
            'etextbook': etextbook,
            'chapter': chapter,
            'lesson': lesson,
            'content_blocks': content_blocks,
            'assets': assets,
            'dependencies': dependencies,
            'export_date': datetime.now().isoformat(),
            'hierarchy': self.query_full_hierarchy(lesson_id)
        }
        
        with open(output_path, 'w') as f:
            json.dump(manifest, f, indent=2)
            
        print(f"✅ Complete manifest exported to {output_path}")
        return manifest
        
    def generate_asset_spec_report(self, lesson_id):
        """Generate detailed asset specification report"""
        cursor = self.conn.cursor()
        
        cursor.execute("""
            SELECT 
                a.asset_id,
                a.filename,
                a.asset_type,
                a.format,
                a.width_px,
                a.height_px,
                a.alt_text,
                GROUP_CONCAT(s.spec_name || ': ' || s.spec_value || ' (' || s.priority || ')') as specs
            FROM assets a
            LEFT JOIN specifications s ON a.asset_id = s.asset_id
            WHERE a.lesson_id = ?
            GROUP BY a.asset_id
            ORDER BY a.asset_type, a.filename
        """, (lesson_id,))
        
        assets = cursor.fetchall()
        
        print(f"\n📋 ASSET SPECIFICATION REPORT: {lesson_id}")
        print("=" * 100)
        
        for asset in assets:
            print(f"\n{asset['filename']}")
            print(f"  Type: {asset['asset_type']} | Format: {asset['format']}")
            if asset['width_px']:
                print(f"  Size: {asset['width_px']}×{asset['height_px']} px")
            print(f"  Alt: {asset['alt_text']}")
            if asset['specs']:
                print(f"  Specs: {asset['specs']}")
            print("-" * 100)
        
        return assets
        
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()


def initialize_ssot_system():
    """Initialize complete SSOT database system"""
    print("=" * 80)
    print("🗄️  MESO CURRICULUM - SSOT DATABASE SYSTEM")
    print("=" * 80)
    print()
    
    db = SSOTDatabase()
    db.connect()
    db.create_complete_schema()
    db.seed_sample_data()
    
    print("\n📊 DATABASE STRUCTURE")
    print("-" * 80)
    print("LEVEL 1: SSOTs (Single Source of Truth)")
    print("LEVEL 2: eTextbooks")
    print("LEVEL 3: Chapters")
    print("LEVEL 4: Lessons")
    print("LEVEL 5: Content Blocks")
    print("LEVEL 6: Assets")
    print("LEVEL 7: Specifications")
    print()
    print("Supporting: Sections, Slides, Overlays, Standards, Tags, Dependencies")
    print()
    
    # Query sample data
    print("🔍 SAMPLE QUERY: G3-1B Hierarchy")
    print("-" * 80)
    hierarchy = db.query_full_hierarchy('G3-1B')
    if hierarchy:
        print(f"SSOT: {hierarchy['ssot_title']}")
        print(f"  └─ eTextbook: {hierarchy['etextbook_title']}")
        print(f"      └─ Chapter: {hierarchy['chapter_title']}")
        print(f"          └─ Lesson: {hierarchy['lesson_name']}")
        print(f"              ├─ Content Blocks: {hierarchy['content_blocks']}")
        print(f"              ├─ Assets: {hierarchy['assets']}")
        print(f"              └─ Specifications: {hierarchy['specifications']}")
    
    # Export manifest
    print("\n📦 EXPORTING MANIFEST")
    print("-" * 80)
    manifest = db.export_complete_manifest('G3-1B', 'G3_1B_complete_manifest.json')
    
    # Generate spec report
    print("\n📋 ASSET SPECIFICATION REPORT")
    print("-" * 80)
    db.generate_asset_spec_report('G3-1B')
    
    db.close()
    
    print("\n" + "=" * 80)
    print("✅ SSOT DATABASE SYSTEM COMPLETE")
    print("=" * 80)
    print(f"📦 Database: meso_ssot_complete.db")
    print(f"📄 Manifest: G3_1B_complete_manifest.json")
    print()
    print("Tables created: 14")
    print("  - ssots, etextbooks, chapters, lessons")
    print("  - content_blocks, assets, specifications")
    print("  - sections, slides, overlays, standards")
    print("  - tags, dependencies, production_status")
    print()


if __name__ == '__main__':
    initialize_ssot_system()
