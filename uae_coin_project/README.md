# UAE Commemorative Coin Project - QR Code System

This directory contains the QR code generation system for the UAE Commemorative Coin Project. The system generates QR codes that link to emirate-specific pages, cultural content, project documentation, and downloadable assets.

## 🎯 Purpose

Generate QR codes for embedding in:
- Formal documents
- Project web pages
- Commemorative coins (physical or digital)
- Marketing materials
- Documentation

## 📱 QR Code Destinations

### Live at Minting
1. **Emirate 1 (Abu Dhabi)** - `https://u.ae/abudhabi`
2. **Emirate 2 (Dubai)** - `https://u.ae/dubai`
3. **Falcon Eye (Culture)** - `https://u.ae/culture`

### Project Resources
4. **Project Web Page** - GitHub repository
5. **Documentation** - Technical documentation
6. **Downloadable 3D Model** - Release assets

## 🚀 Quick Start

### Prerequisites

```bash
# Install required dependencies
pip install qrcode[pil] pillow>=10.3.0
```

### Generate QR Codes

```bash
# Navigate to the project directory
cd uae_coin_project

# Run the QR code generator
python generate_qr_codes.py
```

### Output

The script generates:
- **PNG files** - High-quality raster images for documents and print
- **SVG files** - Vector images for web and scalable applications
- **Summary report** - Markdown documentation with previews

Files are saved to:
```
uae_coin_project/
├── qr_codes/
│   ├── emirate1_abudhabi_qr.png
│   ├── emirate1_abudhabi_qr.svg
│   ├── emirate2_dubai_qr.png
│   ├── emirate2_dubai_qr.svg
│   ├── falcon_eye_culture_qr.png
│   ├── falcon_eye_culture_qr.svg
│   ├── project_webpage_qr.png
│   ├── project_webpage_qr.svg
│   ├── documentation_qr.png
│   ├── documentation_qr.svg
│   ├── downloadable_3d_model_qr.png
│   └── downloadable_3d_model_qr.svg
└── docs/
    └── QR_CODES_SUMMARY.md
```

## 📖 Documentation

- **[QR Codes Summary](docs/QR_CODES_SUMMARY.md)** - Overview of all generated QR codes with previews
- **[Update Instructions](docs/UPDATE_QR_DESTINATIONS.md)** - Guide for updating QR code destinations

## 🔧 Customization

### Updating URLs

Edit `generate_qr_codes.py` and modify the `QR_DESTINATIONS` dictionary:

```python
QR_DESTINATIONS = {
    'emirate1_abudhabi': {
        'url': 'https://u.ae/abudhabi',  # Change this URL
        'description': 'Emirate 1 (Abu Dhabi) - Live at minting',
        'filename': 'emirate1_abudhabi_qr'
    },
    # ... more entries
}
```

Then regenerate:
```bash
python generate_qr_codes.py
```

### Adjusting QR Code Appearance

Modify parameters in the generator methods:

```python
# For PNG
generator.generate_qr_png(url, filename, box_size=10, border=4)

# For SVG
generator.generate_qr_svg(url, filename, box_size='10mm', border=4)
```

## 💡 Usage Examples

### Embedding in HTML

```html
<!-- Using PNG -->
<img src="qr_codes/emirate1_abudhabi_qr.png" alt="Abu Dhabi QR Code" width="200">

<!-- Using SVG (recommended for web) -->
<img src="qr_codes/emirate1_abudhabi_qr.svg" alt="Abu Dhabi QR Code" width="200">
```

### Embedding in Markdown

```markdown
![Abu Dhabi QR Code](qr_codes/emirate1_abudhabi_qr.png)
```

### Embedding in LaTeX/PDF Documents

```latex
\includegraphics[width=3cm]{qr_codes/emirate1_abudhabi_qr.png}
```

### Using in Python

```python
from generate_qr_codes import UAECoinQRGenerator

# Create generator
generator = UAECoinQRGenerator(output_dir='my_qr_codes')

# Generate a single QR code
generator.generate_qr_png('https://example.com', 'my_qr_code')

# Generate all QR codes
results = generator.generate_all_qr_codes()
```

## ✅ Best Practices

### For Print Materials
- Use PNG format at 300+ DPI
- Ensure minimum size of 2cm x 2cm for reliable scanning
- Test print quality before mass production
- Maintain white border (quiet zone) of at least 4 modules

### For Digital Display
- Use SVG format for scalability
- Ensure responsive design on mobile devices
- Test on multiple screen sizes
- Provide fallback link text below QR code

### For Physical Coins
- Consider surface finish and scanning conditions
- Test under various lighting conditions
- Use high error correction (already enabled)
- Position QR code on flat surface area

## 🔒 Security Considerations

- All URLs use HTTPS for secure connections
- High error correction (30%) enables scanning even with minor damage
- URLs are publicly accessible (no authentication required)
- No personal or sensitive information encoded in QR codes

## 🧪 Testing

Validate QR code generation:

```bash
# Run the generator and verify output
python generate_qr_codes.py

# Check that all files were created
ls -la qr_codes/

# Verify the summary report was generated
cat docs/QR_CODES_SUMMARY.md
```

Test QR codes:
1. Scan each QR code with multiple smartphones
2. Test on both iOS and Android devices
3. Verify destination URLs load correctly
4. Check mobile responsiveness of destination pages

## 📊 Technical Specifications

- **Error Correction**: Level H (High) - 30% recovery
- **QR Code Version**: Auto-adjusted based on data length
- **Box Size**: 10px (PNG) / 10mm (SVG)
- **Border**: 4 modules (standard quiet zone)
- **Color Scheme**: Black on white for maximum contrast
- **Image Formats**: PNG (raster) and SVG (vector)

## 🔄 Post-Deployment Updates

After QR codes are deployed (printed/embedded):

1. **URL Redirects**: Use redirects to change destinations without regenerating QR codes
2. **Content Updates**: Update content at destination URLs
3. **Analytics**: Monitor QR code scans using URL tracking

See [UPDATE_QR_DESTINATIONS.md](docs/UPDATE_QR_DESTINATIONS.md) for detailed instructions.

## 📝 License

This QR code generation system is part of the Activbot project.
See the main [LICENSE](../LICENSE) file for details.

## 🤝 Contributing

To add new QR codes or improve the system:

1. Edit `generate_qr_codes.py`
2. Add new entries to `QR_DESTINATIONS`
3. Regenerate QR codes
4. Update documentation
5. Submit a pull request

## 📞 Support

For issues or questions:
- GitHub Issues: https://github.com/ELMOURABEA/Activbot/issues
- Documentation: See main README.md

---

**Generated by Activbot QR Code System** 🇦🇪
