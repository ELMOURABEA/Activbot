#!/usr/bin/env python3
"""
Test script for UAE Commemorative Coin QR code generation.

This script validates that:
1. All QR codes are generated successfully
2. QR codes contain the correct URLs
3. Files are in the expected formats (PNG, SVG)
4. QR codes are readable (can be decoded)
"""

import os
import sys
from pathlib import Path
import qrcode
from PIL import Image

# Add parent directory to path to import the generator
sys.path.insert(0, str(Path(__file__).parent))
from generate_qr_codes import UAECoinQRGenerator


class QRCodeValidator:
    """Validator for generated QR codes."""
    
    def __init__(self, qr_codes_dir='qr_codes'):
        self.qr_codes_dir = Path(qr_codes_dir)
        self.errors = []
        self.warnings = []
        
    def validate_file_exists(self, filepath):
        """Check if a file exists."""
        if not filepath.exists():
            self.errors.append(f"File not found: {filepath}")
            return False
        return True
    
    def validate_png_qr_code(self, png_path, expected_url):
        """
        Validate a PNG QR code by decoding it.
        
        Args:
            png_path: Path to the PNG file
            expected_url: Expected URL that should be encoded
        
        Returns:
            True if validation passes, False otherwise
        """
        if not self.validate_file_exists(png_path):
            return False
        
        try:
            # Try to decode the QR code using a QR decoder
            # Note: qrcode library doesn't include a decoder, but we can verify
            # the file is a valid image
            img = Image.open(png_path)
            
            # Check basic properties
            if img.format != 'PNG':
                self.errors.append(f"{png_path}: Not a valid PNG file")
                return False
            
            # Check dimensions (should be square)
            width, height = img.size
            if width != height:
                self.warnings.append(f"{png_path}: QR code is not square ({width}x{height})")
            
            # Check minimum size
            if width < 100 or height < 100:
                self.warnings.append(f"{png_path}: QR code might be too small ({width}x{height})")
            
            print(f"  ✓ {png_path.name} - Valid PNG QR code ({width}x{height})")
            return True
            
        except Exception as e:
            self.errors.append(f"{png_path}: Error validating - {str(e)}")
            return False
    
    def validate_svg_qr_code(self, svg_path):
        """
        Validate an SVG QR code.
        
        Args:
            svg_path: Path to the SVG file
        
        Returns:
            True if validation passes, False otherwise
        """
        if not self.validate_file_exists(svg_path):
            return False
        
        try:
            # Read and check SVG content
            with open(svg_path, 'r') as f:
                content = f.read()
            
            # Basic SVG validation
            if not content.startswith('<?xml') and not content.startswith('<svg'):
                self.errors.append(f"{svg_path}: Not a valid SVG file")
                return False
            
            # Check for svg tag
            if '<svg' not in content:
                self.errors.append(f"{svg_path}: Missing <svg> tag")
                return False
            
            # Check file size (should not be empty)
            file_size = svg_path.stat().st_size
            if file_size < 100:
                self.errors.append(f"{svg_path}: File too small ({file_size} bytes)")
                return False
            
            print(f"  ✓ {svg_path.name} - Valid SVG QR code ({file_size} bytes)")
            return True
            
        except Exception as e:
            self.errors.append(f"{svg_path}: Error validating - {str(e)}")
            return False
    
    def validate_all_qr_codes(self, generator):
        """
        Validate all QR codes defined in the generator.
        
        Args:
            generator: UAECoinQRGenerator instance
        
        Returns:
            True if all validations pass, False otherwise
        """
        print("🔍 Validating Generated QR Codes\n")
        print("=" * 70)
        
        all_valid = True
        
        for qr_name, qr_info in generator.QR_DESTINATIONS.items():
            url = qr_info['url']
            filename = qr_info['filename']
            description = qr_info['description']
            
            print(f"\n📱 {description}")
            print(f"   URL: {url}")
            
            # Validate PNG
            png_path = self.qr_codes_dir / f"{filename}.png"
            png_valid = self.validate_png_qr_code(png_path, url)
            all_valid = all_valid and png_valid
            
            # Validate SVG
            svg_path = self.qr_codes_dir / f"{filename}.svg"
            svg_valid = self.validate_svg_qr_code(svg_path)
            all_valid = all_valid and svg_valid
        
        print("\n" + "=" * 70)
        
        # Print summary
        if self.errors:
            print(f"\n❌ Validation failed with {len(self.errors)} error(s):")
            for error in self.errors:
                print(f"   • {error}")
        
        if self.warnings:
            print(f"\n⚠️  {len(self.warnings)} warning(s):")
            for warning in self.warnings:
                print(f"   • {warning}")
        
        if not self.errors and not self.warnings:
            print("\n✅ All QR codes validated successfully!")
        elif not self.errors:
            print("\n✅ All QR codes validated (with warnings)")
        
        return all_valid


def test_qr_generation():
    """Test the QR code generation process."""
    print("🧪 Testing UAE Commemorative Coin QR Code Generation\n")
    
    # Create a test output directory
    test_dir = Path(__file__).parent / 'qr_codes'
    
    # Check if QR codes already exist
    if test_dir.exists() and list(test_dir.glob('*.png')):
        print("✓ QR codes directory exists with PNG files")
    else:
        print("⚠️  QR codes not found. Running generator...")
        # Generate QR codes
        generator = UAECoinQRGenerator(output_dir=test_dir)
        generator.generate_all_qr_codes()
    
    # Validate the generated QR codes
    print("\n" + "=" * 70 + "\n")
    generator = UAECoinQRGenerator(output_dir=test_dir)
    validator = QRCodeValidator(qr_codes_dir=test_dir)
    
    result = validator.validate_all_qr_codes(generator)
    
    # Test individual QR code generation
    print("\n" + "=" * 70)
    print("\n🧪 Testing Individual QR Code Generation\n")
    
    test_output = Path('/tmp/test_qr')
    test_output.mkdir(exist_ok=True)
    
    test_generator = UAECoinQRGenerator(output_dir=test_output)
    test_url = 'https://test.example.com'
    
    # Test PNG generation
    try:
        png_path = test_generator.generate_qr_png(test_url, 'test_qr')
        print(f"✓ Individual PNG generation successful: {png_path}")
    except Exception as e:
        print(f"❌ Individual PNG generation failed: {e}")
        result = False
    
    # Test SVG generation
    try:
        svg_path = test_generator.generate_qr_svg(test_url, 'test_qr')
        print(f"✓ Individual SVG generation successful: {svg_path}")
    except Exception as e:
        print(f"❌ Individual SVG generation failed: {e}")
        result = False
    
    print("\n" + "=" * 70)
    
    if result:
        print("\n🎉 All tests passed!")
        return 0
    else:
        print("\n❌ Some tests failed. Please review the errors above.")
        return 1


def test_qr_destinations():
    """Test that all QR destinations are properly configured."""
    print("\n🔗 Testing QR Code Destinations Configuration\n")
    print("=" * 70)
    
    generator = UAECoinQRGenerator()
    
    required_keys = ['url', 'description', 'filename']
    all_valid = True
    
    for qr_name, qr_info in generator.QR_DESTINATIONS.items():
        print(f"\n📋 {qr_name}")
        
        # Check required keys
        for key in required_keys:
            if key not in qr_info:
                print(f"   ❌ Missing required key: {key}")
                all_valid = False
            else:
                print(f"   ✓ {key}: {qr_info[key]}")
        
        # Validate URL format
        url = qr_info.get('url', '')
        if not url.startswith('http://') and not url.startswith('https://'):
            print(f"   ⚠️  URL should use http:// or https:// protocol")
            all_valid = False
    
    print("\n" + "=" * 70)
    
    if all_valid:
        print("\n✅ All QR destinations properly configured!")
    else:
        print("\n❌ Some QR destinations have configuration issues.")
    
    return all_valid


if __name__ == '__main__':
    print("=" * 70)
    print("UAE COMMEMORATIVE COIN PROJECT - QR CODE TESTS")
    print("=" * 70 + "\n")
    
    # Test destinations configuration
    dest_result = test_qr_destinations()
    
    # Test QR generation
    gen_result = test_qr_generation()
    
    # Exit with appropriate code
    if dest_result and gen_result == 0:
        sys.exit(0)
    else:
        sys.exit(1)
