#!/usr/bin/env python3
"""
QR Code Generator for UAE Commemorative Coin Project

This script generates QR codes for the UAE Commemorative Coin Project, linking to:
- Emirate-specific pages (Abu Dhabi, Dubai)
- Cultural content (Falcon eye)
- Project documentation and assets

QR codes are generated in both PNG and SVG formats for versatility.
"""

import os
import qrcode
import qrcode.image.svg
from pathlib import Path


class UAECoinQRGenerator:
    """Generator for UAE Commemorative Coin Project QR codes."""
    
    # QR code destinations
    QR_DESTINATIONS = {
        'emirate1_abudhabi': {
            'url': 'https://u.ae/abudhabi',
            'description': 'Emirate 1 (Abu Dhabi) - Live at minting',
            'filename': 'emirate1_abudhabi_qr'
        },
        'emirate2_dubai': {
            'url': 'https://u.ae/dubai',
            'description': 'Emirate 2 (Dubai) - Live at minting',
            'filename': 'emirate2_dubai_qr'
        },
        'falcon_eye_culture': {
            'url': 'https://u.ae/culture',
            'description': 'Falcon Eye - Cultural Heritage',
            'filename': 'falcon_eye_culture_qr'
        },
        'project_webpage': {
            'url': 'https://github.com/ELMOURABEA/Activbot',
            'description': 'Project Web Page',
            'filename': 'project_webpage_qr'
        },
        'documentation': {
            'url': 'https://github.com/ELMOURABEA/Activbot/blob/main/README.md',
            'description': 'Project Documentation',
            'filename': 'documentation_qr'
        },
        'downloadable_3d_model': {
            'url': 'https://github.com/ELMOURABEA/Activbot/releases',
            'description': 'Downloadable 3D Model and Assets',
            'filename': 'downloadable_3d_model_qr'
        }
    }
    
    def __init__(self, output_dir='qr_codes'):
        """
        Initialize the QR code generator.
        
        Args:
            output_dir: Directory where QR codes will be saved
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def generate_qr_png(self, url, filename, box_size=10, border=4):
        """
        Generate a QR code in PNG format.
        
        Args:
            url: The URL to encode in the QR code
            filename: Base filename (without extension)
            box_size: Size of each box in pixels (default: 10)
            border: Border size in boxes (default: 4)
        
        Returns:
            Path to the generated PNG file
        """
        qr = qrcode.QRCode(
            version=1,  # Starting version, will auto-adjust when fit=True
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
            box_size=box_size,
            border=border,
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        output_path = self.output_dir / f"{filename}.png"
        img.save(output_path)
        
        return output_path
    
    def generate_qr_svg(self, url, filename, box_size=10, border=4):
        """
        Generate a QR code in SVG format.
        
        Args:
            url: The URL to encode in the QR code
            filename: Base filename (without extension)
            box_size: Size of each box in pixels (default: 10)
            border: Border size in boxes (default: 4)
        
        Returns:
            Path to the generated SVG file
        """
        factory = qrcode.image.svg.SvgPathImage
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=box_size,
            border=border,
            image_factory=factory
        )
        qr.add_data(url)
        qr.make(fit=True)
        
        img = qr.make_image()
        
        output_path = self.output_dir / f"{filename}.svg"
        with open(output_path, 'wb') as f:
            img.save(f)
        
        return output_path
    
    def generate_all_qr_codes(self):
        """
        Generate all QR codes for the UAE Commemorative Coin Project.
        
        Returns:
            Dictionary mapping QR code names to their file paths
        """
        results = {}
        
        print("🇦🇪 Generating QR Codes for UAE Commemorative Coin Project\n")
        print("=" * 70)
        
        for qr_name, qr_info in self.QR_DESTINATIONS.items():
            url = qr_info['url']
            filename = qr_info['filename']
            description = qr_info['description']
            
            print(f"\n📱 {description}")
            print(f"   URL: {url}")
            
            # Generate PNG
            png_path = self.generate_qr_png(url, filename)
            print(f"   ✓ PNG: {png_path}")
            
            # Generate SVG
            svg_path = self.generate_qr_svg(url, filename)
            print(f"   ✓ SVG: {svg_path}")
            
            results[qr_name] = {
                'png': str(png_path),
                'svg': str(svg_path),
                'url': url,
                'description': description
            }
        
        print("\n" + "=" * 70)
        print(f"✅ Successfully generated {len(results)} QR codes")
        print(f"📁 Output directory: {self.output_dir.absolute()}\n")
        
        return results
    
    def generate_summary_report(self, results):
        """
        Generate a summary report of all generated QR codes.
        
        Args:
            results: Dictionary of generated QR codes
        
        Returns:
            Path to the summary report
        """
        report_path = self.output_dir.parent / 'docs' / 'QR_CODES_SUMMARY.md'
        report_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(report_path, 'w') as f:
            f.write("# UAE Commemorative Coin Project - QR Codes Summary\n\n")
            f.write("This document provides an overview of all generated QR codes for the UAE Commemorative Coin Project.\n\n")
            f.write("## Generated QR Codes\n\n")
            
            for qr_name, info in results.items():
                f.write(f"### {info['description']}\n\n")
                f.write(f"**Destination URL:** `{info['url']}`\n\n")
                f.write(f"**Files Generated:**\n")
                f.write(f"- PNG: `{info['png']}`\n")
                f.write(f"- SVG: `{info['svg']}`\n\n")
                f.write(f"**QR Code Preview (PNG):**\n\n")
                f.write(f"![{info['description']}]({os.path.relpath(info['png'], report_path.parent)})\n\n")
                f.write("---\n\n")
            
            f.write("## Usage Instructions\n\n")
            f.write("### Embedding in Documents\n\n")
            f.write("#### For PDF Documents\n")
            f.write("Use the PNG format files for embedding in PDF documents.\n\n")
            f.write("#### For Web Pages\n")
            f.write("Use the SVG format files for crisp rendering on web pages at any scale.\n\n")
            f.write("#### For Print Materials\n")
            f.write("Use the PNG files with high DPI settings (300+ DPI recommended for professional printing).\n\n")
            f.write("### Scanning QR Codes\n\n")
            f.write("QR codes can be scanned using:\n")
            f.write("- Smartphone camera apps (most modern phones have built-in QR scanning)\n")
            f.write("- Dedicated QR code scanner apps\n")
            f.write("- Web browsers with QR scanning features\n\n")
            f.write("## Technical Details\n\n")
            f.write("- **Error Correction Level:** High (H) - 30% of codewords can be restored\n")
            f.write("- **Format:** PNG (raster) and SVG (vector)\n")
            f.write("- **Border Size:** 4 modules (standard QR code quiet zone)\n")
            f.write("- **Color Scheme:** Black on white for maximum contrast and readability\n\n")
            
        print(f"📄 Summary report generated: {report_path}")
        return report_path


def main():
    """Main entry point for QR code generation."""
    # Determine script location and set output directory
    script_dir = Path(__file__).parent
    output_dir = script_dir / 'qr_codes'
    
    # Create generator instance
    generator = UAECoinQRGenerator(output_dir=output_dir)
    
    # Generate all QR codes
    results = generator.generate_all_qr_codes()
    
    # Generate summary report
    generator.generate_summary_report(results)
    
    print("🎉 QR code generation complete!")
    print("📖 See docs/QR_CODES_SUMMARY.md for detailed information")


if __name__ == '__main__':
    main()
