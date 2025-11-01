# QR Code Integration Examples

This document provides practical examples of how to embed the generated QR codes in various types of documents and applications.

## Table of Contents

1. [HTML/Web Pages](#htmlweb-pages)
2. [Markdown Documents](#markdown-documents)
3. [LaTeX/PDF Documents](#latexpdf-documents)
4. [Microsoft Word Documents](#microsoft-word-documents)
5. [PowerPoint Presentations](#powerpoint-presentations)
6. [Email Templates](#email-templates)
7. [Social Media](#social-media)

---

## HTML/Web Pages

### Basic Embedding

```html
<!DOCTYPE html>
<html>
<head>
    <title>UAE Commemorative Coin Project</title>
</head>
<body>
    <h1>UAE Commemorative Coin Project</h1>
    
    <!-- Using PNG -->
    <div class="qr-code">
        <h2>Emirate 1: Abu Dhabi</h2>
        <img src="../qr_codes/emirate1_abudhabi_qr.png" 
             alt="Abu Dhabi QR Code" 
             width="200" 
             height="200">
        <p>Scan to learn more about Abu Dhabi</p>
    </div>
    
    <!-- Using SVG (recommended for web) -->
    <div class="qr-code">
        <h2>Emirate 2: Dubai</h2>
        <img src="../qr_codes/emirate2_dubai_qr.svg" 
             alt="Dubai QR Code" 
             width="200" 
             height="200">
        <p>Scan to learn more about Dubai</p>
    </div>
</body>
</html>
```

### Responsive Design

```html
<style>
    .qr-container {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: center;
    }
    
    .qr-card {
        text-align: center;
        padding: 20px;
        border: 1px solid #ddd;
        border-radius: 8px;
        max-width: 250px;
    }
    
    .qr-card img {
        width: 100%;
        max-width: 200px;
        height: auto;
    }
    
    @media (max-width: 768px) {
        .qr-card {
            max-width: 100%;
        }
    }
</style>

<div class="qr-container">
    <div class="qr-card">
        <h3>Abu Dhabi</h3>
        <img src="../qr_codes/emirate1_abudhabi_qr.svg" alt="Abu Dhabi">
        <p>Scan for emirate info</p>
    </div>
    
    <div class="qr-card">
        <h3>Dubai</h3>
        <img src="../qr_codes/emirate2_dubai_qr.svg" alt="Dubai">
        <p>Scan for emirate info</p>
    </div>
    
    <div class="qr-card">
        <h3>Cultural Heritage</h3>
        <img src="../qr_codes/falcon_eye_culture_qr.svg" alt="Culture">
        <p>Scan for cultural content</p>
    </div>
</div>
```

### With Fallback Links

```html
<div class="qr-section">
    <img src="../qr_codes/project_webpage_qr.svg" 
         alt="Project Website QR Code"
         width="200">
    <p>
        <strong>Scan to visit our website</strong><br>
        Or visit: <a href="https://github.com/ELMOURABEA/Activbot">
            github.com/ELMOURABEA/Activbot
        </a>
    </p>
</div>
```

---

## Markdown Documents

### Basic Embedding

```markdown
# UAE Commemorative Coin Project

## Quick Access QR Codes

### Emirate 1: Abu Dhabi
![Abu Dhabi QR Code](../qr_codes/emirate1_abudhabi_qr.png)

Scan this QR code to learn more about Abu Dhabi's heritage and role in the UAE.

### Emirate 2: Dubai
![Dubai QR Code](../qr_codes/emirate2_dubai_qr.png)

Scan this QR code to discover Dubai's contributions to the nation.

### Cultural Heritage
![Falcon Eye QR Code](../qr_codes/falcon_eye_culture_qr.png)

Explore the cultural significance of the falcon in UAE heritage.
```

### With Tables

```markdown
| Category | QR Code | Description |
|----------|---------|-------------|
| Abu Dhabi | ![Abu Dhabi](../qr_codes/emirate1_abudhabi_qr.png) | Emirate information |
| Dubai | ![Dubai](../qr_codes/emirate2_dubai_qr.png) | Emirate information |
| Culture | ![Culture](../qr_codes/falcon_eye_culture_qr.png) | Cultural heritage |
```

### GitHub README Integration

```markdown
## Quick Links via QR Codes

<table>
  <tr>
    <td align="center">
      <img src="uae_coin_project/qr_codes/project_webpage_qr.png" width="150"><br>
      <b>Project Website</b>
    </td>
    <td align="center">
      <img src="uae_coin_project/qr_codes/documentation_qr.png" width="150"><br>
      <b>Documentation</b>
    </td>
    <td align="center">
      <img src="uae_coin_project/qr_codes/downloadable_3d_model_qr.png" width="150"><br>
      <b>Download Assets</b>
    </td>
  </tr>
</table>
```

---

## LaTeX/PDF Documents

### Basic Embedding

```latex
\documentclass{article}
\usepackage{graphicx}
\usepackage{hyperref}

\begin{document}

\section{UAE Commemorative Coin Project}

\subsection{Emirate 1: Abu Dhabi}

Scan the QR code below to learn more:

\begin{center}
\includegraphics[width=3cm]{../qr_codes/emirate1_abudhabi_qr.png}
\end{center}

\subsection{Project Resources}

\begin{figure}[h]
\centering
\begin{tabular}{ccc}
\includegraphics[width=3cm]{../qr_codes/project_webpage_qr.png} &
\includegraphics[width=3cm]{../qr_codes/documentation_qr.png} &
\includegraphics[width=3cm]{../qr_codes/downloadable_3d_model_qr.png} \\
Website & Documentation & Downloads
\end{tabular}
\caption{Project QR Codes}
\end{figure}

\end{document}
```

### Professional Document Layout

```latex
\documentclass[12pt]{article}
\usepackage{graphicx}
\usepackage{float}
\usepackage{caption}

\begin{document}

\section{Quick Reference Guide}

\begin{figure}[H]
\centering
\fbox{\includegraphics[width=4cm]{../qr_codes/emirate1_abudhabi_qr.png}}
\caption{Abu Dhabi Emirate Information - \url{https://u.ae/abudhabi}}
\end{figure}

\noindent\textbf{Note:} Scan with any QR code reader or smartphone camera.

\end{document}
```

---

## Microsoft Word Documents

### Method 1: Insert as Picture

1. Click **Insert** → **Pictures** → **This Device**
2. Navigate to `uae_coin_project/qr_codes/`
3. Select the PNG file (e.g., `emirate1_abudhabi_qr.png`)
4. Click **Insert**
5. Resize as needed (right-click → **Size and Position**)

### Method 2: Drag and Drop

1. Open your Word document
2. Open File Explorer and navigate to the QR codes folder
3. Drag the PNG file directly into the document
4. Position and resize as needed

### Layout Example

```
┌─────────────────────────────────────┐
│  UAE Commemorative Coin Project     │
├─────────────────────────────────────┤
│                                     │
│  Emirate 1: Abu Dhabi              │
│  ┌─────────┐                       │
│  │  [QR]   │  Scan to learn more   │
│  │  CODE   │  about Abu Dhabi      │
│  └─────────┘                       │
│                                     │
└─────────────────────────────────────┘
```

### Best Practices for Word

- Use **PNG format** for better compatibility
- Set image size to **2-3 cm** for printed documents
- Use **In Line with Text** or **Square** wrapping
- Add caption using **References** → **Insert Caption**

---

## PowerPoint Presentations

### Slide Layout

```
Slide 1: Title Slide
┌────────────────────────────────┐
│                                │
│  UAE Commemorative Coin        │
│  Project                       │
│                                │
│  [Large QR Code]               │
│                                │
└────────────────────────────────┘

Slide 2: Multiple QR Codes
┌────────────────────────────────┐
│  Quick Access                  │
│                                │
│  [QR1]  [QR2]  [QR3]          │
│  Abu     Dubai  Culture        │
│  Dhabi                         │
└────────────────────────────────┘
```

### PowerPoint Instructions

1. **Insert QR Code:**
   - Insert → Pictures → select PNG file
   - Resize to 3-5 cm for visibility

2. **Add Animation:**
   - Animations → Fade In
   - Effect Options → After Previous

3. **Add Hyperlink (optional):**
   - Right-click QR code → Hyperlink
   - Enter the destination URL

### Presenter Notes Template

```
Slide Notes:
- QR code links to: [URL]
- Audience can scan during or after presentation
- Handout includes all QR codes
- Live demo available if needed
```

---

## Email Templates

### HTML Email

```html
<!DOCTYPE html>
<html>
<body style="font-family: Arial, sans-serif;">
    <h2>UAE Commemorative Coin Project</h2>
    
    <p>Dear Stakeholder,</p>
    
    <p>We're excited to share the UAE Commemorative Coin Project resources:</p>
    
    <table cellpadding="10">
        <tr>
            <td align="center">
                <img src="cid:qr_project_webpage" width="150" alt="Project Website">
                <br><strong>Project Website</strong>
            </td>
            <td align="center">
                <img src="cid:qr_documentation" width="150" alt="Documentation">
                <br><strong>Documentation</strong>
            </td>
        </tr>
    </table>
    
    <p>Or visit directly: 
        <a href="https://github.com/ELMOURABEA/Activbot">
            github.com/ELMOURABEA/Activbot
        </a>
    </p>
    
    <p>Best regards,<br>The UAE Coin Project Team</p>
</body>
</html>
```

### Plain Text Email

```
Subject: UAE Commemorative Coin Project - Quick Access

Dear Stakeholder,

Access the UAE Commemorative Coin Project resources:

Project Website: https://github.com/ELMOURABEA/Activbot
Documentation: https://github.com/ELMOURABEA/Activbot/blob/main/README.md
Downloads: https://github.com/ELMOURABEA/Activbot/releases

QR codes are attached for easy mobile access.

Best regards,
The UAE Coin Project Team

---
[QR codes attached as images]
```

---

## Social Media

### Instagram/Facebook Post

```
📱 UAE Commemorative Coin Project

Scan the QR codes to explore:
🇦🇪 Emirate Information
🦅 Cultural Heritage
📚 Project Documentation

#UAEHeritage #CommemorationCoin #DigitalHeritage
```

**Attach:** Create a collage image with all QR codes using graphic design tools.

### Twitter/X Post

```
🇦🇪 Introducing the UAE Commemorative Coin Project!

Scan the QR code to explore:
✨ Emirate heritage
🦅 Cultural significance
📖 Full documentation

[Attach single QR code image]

#UAE #Heritage #QRCode
```

### LinkedIn Post

```
I'm pleased to share the UAE Commemorative Coin Project, celebrating 
the rich heritage of the United Arab Emirates.

Key Features:
• Interactive QR codes for each emirate
• Cultural heritage resources
• Comprehensive documentation
• Downloadable 3D models

Access all resources via the QR codes in the images below.

#UAEHeritage #Innovation #DigitalTransformation
```

---

## Print Materials

### Business Cards

```
┌─────────────────────────┐
│                         │
│  UAE Commemorative      │
│  Coin Project           │
│                         │
│  [QR CODE]              │
│                         │
│  Scan for details       │
└─────────────────────────┘
```

**Specifications:**
- QR code size: 2cm x 2cm minimum
- Print resolution: 300 DPI or higher
- Use PNG format

### Posters/Banners

```
┌─────────────────────────────────┐
│                                 │
│  UAE COMMEMORATIVE COIN         │
│  PROJECT                        │
│                                 │
│  [Large QR Code - 10cm x 10cm] │
│                                 │
│  SCAN TO EXPLORE                │
│                                 │
└─────────────────────────────────┘
```

### Brochures

**Front Page:** Large featured QR code (5cm x 5cm)
**Inside Pages:** Smaller QR codes (2cm x 2cm) next to relevant sections
**Back Page:** All QR codes in a grid layout with labels

---

## Best Practices Summary

✅ **Use SVG for web** - Scales perfectly at any size
✅ **Use PNG for print** - Better compatibility with office software
✅ **Minimum size: 2cm x 2cm** for reliable scanning
✅ **Test before printing** - Scan on multiple devices
✅ **Include fallback URLs** - Text links for accessibility
✅ **High contrast** - Black on white works best
✅ **Quiet zone** - Keep white space around QR code
✅ **Print at 300+ DPI** - Ensures quality for professional materials

---

## Troubleshooting Common Issues

### QR Code Won't Scan

1. Increase the size of the QR code
2. Ensure good lighting conditions
3. Clean the camera lens
4. Try a different QR code reader app

### Image Quality Issues

1. Use PNG format for print
2. Ensure 300 DPI resolution
3. Don't compress images excessively
4. Re-generate if needed

### Wrong Destination

1. Verify you're using the correct QR code file
2. Check the filename matches the intended destination
3. Re-scan to ensure proper URL

---

For more information, see:
- [QR Codes Summary](QR_CODES_SUMMARY.md)
- [Update Instructions](UPDATE_QR_DESTINATIONS.md)
- [Project README](../README.md)
