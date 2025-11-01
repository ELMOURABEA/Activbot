# 3D Design Package | حزمة التصميم ثلاثي الأبعاد

## UAE 1972-2025 Commemorative Coin

---

## 🎨 3D Design Overview | نظرة عامة على التصميم ثلاثي الأبعاد

This comprehensive 3D design package provides all necessary files and documentation for minting, prototyping, virtual display, and digital twin creation of the UAE Commemorative Coin.

توفر حزمة التصميم ثلاثي الأبعاد الشاملة هذه جميع الملفات والوثائق اللازمة لسك العملة التذكارية للإمارات وصنع نماذجها الأولية وعرضها الافتراضي وإنشاء التوأم الرقمي لها.

---

## 📦 3D File Package Contents | محتويات حزمة الملفات ثلاثية الأبعاد

### Primary 3D Files:

#### 1. **STL Files** (Standard Tessellation Language)
- **Purpose:** 3D printing, CNC machining, die preparation
- **Files Included:**
  - `uae-coin-obverse.stl` - Front side (high-resolution mesh)
  - `uae-coin-reverse.stl` - Back side (high-resolution mesh)
  - `uae-coin-edge.stl` - Edge with serial number template
  - `uae-coin-complete.stl` - Full coin assembly
  - `uae-coin-prototype-low.stl` - Low-poly version for rapid prototyping

**Specifications:**
- Resolution: 0.01mm precision
- Triangle Count: 500,000+ per side (high-res)
- File Format: Binary STL
- Units: Millimeters
- Coordinate System: Z-up

#### 2. **OBJ Files** (Wavefront Object)
- **Purpose:** High-resolution rendering, virtual reality, presentations
- **Files Included:**
  - `uae-coin-obverse-textured.obj` + `.mtl` - With material definitions
  - `uae-coin-reverse-textured.obj` + `.mtl` - With material definitions
  - `uae-coin-complete-textured.obj` + `.mtl` - Full assembly with materials
  - Texture maps (4K resolution):
    - `coin_diffuse_4k.png` - Color map
    - `coin_normal_4k.png` - Normal/bump map
    - `coin_metallic_4k.png` - Metallic map
    - `coin_roughness_4k.png` - Roughness map
    - `coin_ao_4k.png` - Ambient occlusion

**Specifications:**
- Resolution: 0.005mm precision
- Polygon Count: 1,000,000+ per side
- Texture Resolution: 4096 x 4096 pixels
- File Format: ASCII OBJ with MTL
- UV Mapped: Yes, optimized layout

#### 3. **SVG Files** (Scalable Vector Graphics)
- **Purpose:** Scaling, engraving, laser cutting, graphic design
- **Files Included:**
  - `uae-coin-obverse-outline.svg` - Obverse line art
  - `uae-coin-reverse-outline.svg` - Reverse line art
  - `uae-falcon-element.svg` - Isolated falcon design
  - `uae-map-element.svg` - Isolated UAE map
  - `circuit-pattern.svg` - Circuit board pattern
  - `qr-code-zone.svg` - QR code placement guide
  - `typography-arabic.svg` - Arabic calligraphy elements
  - `typography-english.svg` - English text elements

**Specifications:**
- Format: SVG 1.1
- Precision: Vector (infinite scalability)
- Layers: Organized by design element
- Color Space: RGB and spot colors defined
- Export: Compatible with Adobe Illustrator, Inkscape

---

## 🔧 Special Component Files | ملفات المكونات الخاصة

### 1. Bi-Metallic Layering Map
**File:** `bimetallic-layer-diagram.pdf` / `.svg`

**Content:**
- Cross-section view of coin showing material layers
- Gold core dimensions: 30mm diameter, 2.8mm thickness
- Silver ring dimensions: Inner 30mm, outer 50mm, 3.0mm thickness
- Bonding zone specifications
- Material transition details
- Assembly instructions for minting

**Specifications:**
- Gold Core: .999 Fine Gold, 31.1 grams (1 troy oz)
- Silver Ring: .999 Fine Silver, 31.1 grams (1 troy oz)
- Total Weight: 62.2 grams (2 troy oz)
- Bonding Method: Mechanical interlock + laser welding

### 2. Inlay Placement Guide
**File:** `sapphire-inlay-placement.pdf` / `.dwg`

**Content:**
- Precise XYZ coordinates for sapphire placement
- Drilling specifications for inlay cavity
- Depth chart: 0.5mm recess
- Setting instructions
- Quality control checkpoints
- Magnification requirements for placement

**Sapphire Specifications:**
- Stone: Natural blue sapphire
- Cut: Round brilliant
- Diameter: 1.5mm
- Depth: 1.0mm (0.5mm exposed)
- Quality: VS clarity minimum
- Setting: Laser-cut bezel, friction-fit

### 3. QR Zone Logic Map
**File:** `qr-code-integration.svg` / `.ai`

**Content:**
- QR code placement coordinates
- Size and positioning guidelines: 15mm x 15mm
- Error correction level: H (30%)
- Data encoding structure
- Contrast requirements: Black on mirror-polished background
- Scan-ability testing parameters
- Integration with surrounding design elements

**QR Code Details:**
- Version: QR Version 5 (37x37 modules)
- Data: URL + Serial Number
- Format: https://uae-coin-legacy.gov.ae/verify/[SERIAL]
- Module Size: 0.4mm per module
- Quiet Zone: 1.6mm border

---

## 📐 Technical Specifications | المواصفات التقنية

### Master Dimensions:
| Parameter | Value | وحدة القياس |
|-----------|-------|-------------|
| **Diameter** | 50.00mm ± 0.05mm | القطر |
| **Thickness** | 3.00mm ± 0.05mm (center) | السماكة |
| **Edge Thickness** | 3.20mm (raised rim) | سماكة الحافة |
| **Relief Height (Obverse)** | 2.5mm maximum | ارتفاع النقش (أمامي) |
| **Relief Height (Reverse)** | 2.0mm maximum | ارتفاع النقش (خلفي) |
| **Total Weight** | 62.2g ± 0.2g | الوزن الإجمالي |
| **Gold Content** | 31.1g (.999 fine) | محتوى الذهب |
| **Silver Content** | 31.1g (.999 fine) | محتوى الفضة |

### 3D Modeling Specifications:
- **Software Compatibility:** Blender 3.0+, Maya 2020+, 3ds Max 2021+, ZBrush 2022+
- **Coordinate System:** Z-up, right-handed
- **Units:** Millimeters
- **Origin Point:** Center of coin, mid-plane
- **Scale:** 1:1 (actual size)
- **Normals:** Consistent, facing outward
- **Manifold:** Yes, watertight mesh

### Material Definitions (PBR):
```json
{
  "gold_core": {
    "baseColor": [1.0, 0.766, 0.336],
    "metallic": 1.0,
    "roughness": 0.3,
    "ior": 0.47
  },
  "silver_ring": {
    "baseColor": [0.972, 0.960, 0.915],
    "metallic": 1.0,
    "roughness": 0.25,
    "ior": 0.16
  },
  "sapphire_inlay": {
    "baseColor": [0.0, 0.318, 0.729],
    "metallic": 0.0,
    "roughness": 0.05,
    "ior": 1.77,
    "transmission": 0.95
  }
}
```

---

## 🔗 Interactive 3D Viewer Links | روابط العارض ثلاثي الأبعاد التفاعلي

### Official 3D Viewer:
**URL:** https://uae-coin-legacy.gov.ae/3d-viewer

**Features:**
- ✅ Full 360° rotation
- ✅ Zoom in/out (up to 50x magnification)
- ✅ Obverse/Reverse toggle
- ✅ Material viewer (switch between gold, silver views)
- ✅ Annotation hotspots (click for design details)
- ✅ Lighting controls (adjust to see relief details)
- ✅ Screenshot capture
- ✅ VR mode compatible (WebXR)
- ✅ AR preview (view coin in your space via phone)

### Embedding Code:
```html
<iframe 
  src="https://uae-coin-legacy.gov.ae/3d-viewer/embed" 
  width="800" 
  height="600" 
  frameborder="0" 
  allowfullscreen 
  allow="xr-spatial-tracking">
</iframe>
```

### Alternative Platforms:
1. **Sketchfab:** https://sketchfab.com/uae-coin-2025
2. **ArtStation:** https://artstation.com/uae-commemorative-coin
3. **Smithsonian 3D:** [Archived digital heritage]

---

## 💎 Rendering Specifications | مواصفات العرض

### Recommended Render Settings:

#### For Print Materials:
- **Resolution:** 4K minimum (3840 x 2160)
- **DPI:** 300 for print quality
- **Samples:** 2048+ (path tracing)
- **Lighting:** HDRI + 3-point studio setup
- **Output Format:** PNG (16-bit), TIFF, EXR

#### For Digital/Web:
- **Resolution:** 2K (1920 x 1080) or 4K
- **DPI:** 72-150 for screens
- **Samples:** 512-1024
- **Lighting:** Optimized for screen viewing
- **Output Format:** PNG (8-bit), JPEG (high quality)

#### For Animation:
- **Frame Rate:** 30 or 60 FPS
- **Resolution:** 4K for high-end, 1080p for web
- **Format:** MP4 (H.264), ProRes for archival
- **Duration:** 10-30 seconds (full rotation)

### Lighting Setups:
1. **Studio Setup:** 3-point lighting with soft shadows
2. **Museum Setup:** Overhead + accent lighting
3. **Dramatic Setup:** Single key light with rim lighting
4. **Outdoor Setup:** Natural HDRI lighting

---

## 🖨️ 3D Printing Guide | دليل الطباعة ثلاثية الأبعاد

### For Prototyping:

#### Resin Printing (Recommended):
- **Printer:** Formlabs Form 3, Anycubic Photon Mono X
- **Resin:** Castable resin or high-detail resin
- **Layer Height:** 0.025mm
- **Supports:** Minimal, placed on edge
- **Post-Processing:** Wash, cure, polish

#### FDM Printing:
- **Printer:** Prusa i3 MK3S+, Ultimaker S5
- **Material:** PLA or PETG for display, ABS for molds
- **Layer Height:** 0.1mm
- **Infill:** 20% (display), 100% (molds)
- **Supports:** Tree supports recommended

#### Metal Printing (Production):
- **Technology:** DMLS (Direct Metal Laser Sintering)
- **Materials:** Gold alloy, silver alloy
- **Service Providers:** Shapeways, Sculpteo, local mints
- **Post-Processing:** Polishing, plating as needed

### Scale Options:
- **1:1 Scale:** Actual size (50mm diameter) - for mold-making
- **2:1 Scale:** 100mm diameter - for display/presentation
- **5:1 Scale:** 250mm diameter - for trade shows/exhibitions
- **1:2 Scale:** 25mm diameter - for jewelry adaptations

---

## 🎬 Animation & Presentation Files | ملفات الرسوم المتحركة والعرض

### Pre-Rendered Animations:
1. **Rotation Video** (360° spin)
   - Duration: 10 seconds
   - Resolution: 4K
   - Format: MP4 (H.264)
   - File: `uae-coin-rotation-4k.mp4`

2. **Exploded View Animation**
   - Shows bi-metallic layers separating
   - Duration: 15 seconds
   - File: `uae-coin-exploded-view.mp4`

3. **Detail Zoom Sequence**
   - Highlights key features with zoom-ins
   - Duration: 30 seconds
   - File: `uae-coin-details-tour.mp4`

4. **Flip Animation** (Obverse to Reverse)
   - Coin flipping to show both sides
   - Duration: 5 seconds
   - File: `uae-coin-flip.mp4`

---

## 📊 File Download Structure | هيكل تنزيل الملفات

```
3D-Design-Package/
├── STL/
│   ├── high-resolution/
│   │   ├── uae-coin-obverse.stl
│   │   ├── uae-coin-reverse.stl
│   │   └── uae-coin-complete.stl
│   └── low-resolution/
│       └── uae-coin-prototype-low.stl
├── OBJ/
│   ├── models/
│   │   ├── uae-coin-obverse-textured.obj
│   │   ├── uae-coin-reverse-textured.obj
│   │   └── materials.mtl
│   └── textures/
│       ├── coin_diffuse_4k.png
│       ├── coin_normal_4k.png
│       ├── coin_metallic_4k.png
│       ├── coin_roughness_4k.png
│       └── coin_ao_4k.png
├── SVG/
│   ├── uae-coin-obverse-outline.svg
│   ├── uae-coin-reverse-outline.svg
│   ├── design-elements/
│   │   ├── falcon.svg
│   │   ├── map.svg
│   │   └── circuit-pattern.svg
│   └── typography/
│       ├── arabic-text.svg
│       └── english-text.svg
├── special-components/
│   ├── bimetallic-layer-diagram.pdf
│   ├── sapphire-inlay-placement.pdf
│   └── qr-code-integration.svg
├── animations/
│   ├── rotation-4k.mp4
│   ├── exploded-view.mp4
│   ├── details-tour.mp4
│   └── flip.mp4
└── documentation/
    ├── 3d-design-specifications.pdf
    ├── minting-instructions.pdf
    └── material-guide.pdf
```

---

## 🔐 Access & Download | الوصول والتنزيل

### Official Download Portal:
**URL:** https://uae-coin-legacy.gov.ae/downloads/3d-package

**Access Requirements:**
- Verified partner credentials
- Signed NDA (for pre-release access)
- Official mint or production facility verification
- Government authorization (for official use)

### Public Access:
- Low-resolution preview files (watermarked)
- Interactive 3D viewer (web-based)
- Educational models for students
- Reference images for collectors

### للوصول الرسمي:
[Same structure in Arabic]

---

## 🎯 Use Cases | حالات الاستخدام

### 1. Minting & Production:
- Die creation and engraving
- CNC machining setup
- Quality control references
- Production documentation

### 2. Marketing & Presentation:
- Promotional materials
- Trade show displays
- Investor presentations
- Media kits

### 3. Digital Exhibitions:
- Virtual museum displays
- Online galleries
- Educational platforms
- Blockchain metadata

### 4. Research & Education:
- Numismatic studies
- Design analysis
- Student projects
- Heritage preservation

---

## 🌟 Wonderful Touch Details | تفاصيل اللمسة الرائعة

### Zoom-Required Features in 3D:

1. **Feather Micro-Detail** (20x zoom)
   - Individual barbs on falcon feathers
   - Natural texture replication
   - Light-catching surfaces

2. **Circuit Board Traces** (15x zoom)
   - Connection paths as thin as 0.1mm
   - Realistic electronic components
   - Layered depth effect

3. **Calligraphy Flourishes** (25x zoom)
   - Traditional Arabic script beauty
   - Stroke weight variations
   - Decorative terminals

4. **Sapphire Facets** (50x zoom)
   - Brilliant cut faceting
   - Light refraction simulation
   - Crown and pavilion details

5. **Edge Serial Numbers** (10x zoom)
   - Crisp, readable numbering
   - Individual character depth
   - Anti-counterfeit features

6. **Micro-Text Security** (30x zoom)
   - Hidden text in design elements
   - Only visible under magnification
   - "UAE 2025" repeated pattern

---

## 📞 Technical Support | الدعم الفني

For 3D file support, technical questions, or custom requirements:

**Email:** 3d-support@uae-coin-legacy.gov.ae
**Phone:** +971 [X] XXX XXXX
**Portal:** https://uae-coin-legacy.gov.ae/support

**Support Hours:** Sunday - Thursday, 9:00 AM - 5:00 PM GST

---

**Experience the coin in three dimensions - where art meets precision** 🎨🇦🇪

**اختبر العملة في ثلاثة أبعاد - حيث يلتقي الفن بالدقة** ✨
