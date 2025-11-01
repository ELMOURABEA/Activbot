# Updating QR Code Destinations

This guide explains how to update the QR code destinations for the UAE Commemorative Coin Project after deployment.

## Overview

QR codes are immutable once printed or embedded in physical materials. However, you can update the destinations by:

1. **Direct URL Updates**: Modify the script and regenerate QR codes before deployment
2. **URL Redirection**: Use URL shorteners or redirects to change destinations without regenerating QR codes
3. **Dynamic Content**: Update content at the destination URLs without changing the URLs themselves

## Method 1: Regenerating QR Codes (Pre-Deployment)

### Step 1: Edit the QR Code Configuration

Edit the file `uae_coin_project/generate_qr_codes.py` and update the `QR_DESTINATIONS` dictionary:

```python
QR_DESTINATIONS = {
    'emirate1_abudhabi': {
        'url': 'https://u.ae/abudhabi',  # Update this URL
        'description': 'Emirate 1 (Abu Dhabi) - Live at minting',
        'filename': 'emirate1_abudhabi_qr'
    },
    # ... more entries
}
```

### Step 2: Regenerate QR Codes

Run the generator script:

```bash
cd uae_coin_project
python generate_qr_codes.py
```

This will:
- Generate new QR codes with updated URLs
- Overwrite existing QR code files
- Update the summary documentation

### Step 3: Verify Generated QR Codes

Check the generated files in:
- `uae_coin_project/qr_codes/*.png` - PNG format images
- `uae_coin_project/qr_codes/*.svg` - SVG format images

Test the QR codes by scanning them with a smartphone camera or QR code reader.

## Method 2: URL Redirection (Post-Deployment)

If QR codes are already printed or deployed, you can use URL redirection to update destinations without regenerating QR codes.

### Option A: Using u.ae Domain Redirects

Contact the administrators of the u.ae domain to update redirects:

```
Original URL: https://u.ae/abudhabi
Redirect to:  https://new-destination.example.com/abudhabi
```

This allows you to change where users are directed without changing the QR code.

### Option B: Using a URL Shortener Service

1. **Create Short URLs**: Use a URL shortener service (e.g., Bitly, TinyURL, or custom service)
   ```
   Short URL: https://uae.link/coin1
   Current destination: https://u.ae/abudhabi
   ```

2. **Update QR Codes Before Deployment**: Regenerate QR codes using the short URL

3. **Update Destinations Anytime**: Change the destination URL in the shortener service dashboard without changing the QR code

### Option C: Custom Redirect Service

Set up your own redirect service:

1. **Deploy a simple redirect service**:
   ```python
   # Flask example
   from flask import redirect
   
   @app.route('/coin/<id>')
   def redirect_coin(id):
       # Store mappings in database
       destination = get_destination_from_db(id)
       return redirect(destination)
   ```

2. **Update the database** to change destinations without changing QR codes

## Method 3: Dynamic Content Updates

Keep the URLs the same but update the content at those destinations:

1. **Maintain website/page control**: Ensure you have access to update the destination pages
2. **Update content regularly**: Change information, images, or links on the destination pages
3. **No QR code changes needed**: Users scan the same QR code but see updated content

## QR Code Destination Management Best Practices

### Before Deployment

✅ **Test all QR codes** thoroughly before printing or embedding
✅ **Verify URL accessibility** - ensure all URLs are publicly accessible
✅ **Check mobile responsiveness** - destination pages should be mobile-friendly
✅ **Consider using short URLs or redirects** for post-deployment flexibility
✅ **Document all URLs and purposes** in a central registry

### During Deployment

✅ **Use high error correction** (already set to ERROR_CORRECT_H in the script)
✅ **Ensure sufficient quiet zone** (white border) around QR codes
✅ **Print at appropriate resolution** (300+ DPI for professional printing)
✅ **Test scannability** after printing with multiple devices

### After Deployment

✅ **Monitor QR code usage** using analytics on destination pages
✅ **Keep destination URLs live** - maintain server uptime and domain registration
✅ **Update content regularly** to keep users engaged
✅ **Have backup URLs** in case primary destinations become unavailable

## QR Code Testing Checklist

Before finalizing QR codes for production:

- [ ] Scan each QR code with at least 3 different smartphones
- [ ] Test on both iOS and Android devices
- [ ] Verify URLs open correctly in mobile browsers
- [ ] Check mobile page load times
- [ ] Ensure HTTPS is enabled on all destination URLs
- [ ] Test in various lighting conditions (for printed materials)
- [ ] Verify QR codes work at different sizes
- [ ] Test with and without internet connectivity (for error messages)

## Current QR Code Destinations

### Live at Minting URLs

1. **Emirate 1 (Abu Dhabi)**
   - URL: `https://u.ae/abudhabi`
   - Purpose: Information about Abu Dhabi's role in the UAE

2. **Emirate 2 (Dubai)**
   - URL: `https://u.ae/dubai`
   - Purpose: Information about Dubai's role in the UAE

3. **Falcon Eye (Culture)**
   - URL: `https://u.ae/culture`
   - Purpose: Cultural heritage and significance of the falcon

### Project URLs

4. **Project Web Page**
   - URL: `https://github.com/ELMOURABEA/Activbot`
   - Purpose: Main project repository and information

5. **Documentation**
   - URL: `https://github.com/ELMOURABEA/Activbot/blob/main/README.md`
   - Purpose: Technical documentation and usage instructions

6. **Downloadable 3D Model**
   - URL: `https://github.com/ELMOURABEA/Activbot/releases`
   - Purpose: Access to 3D models and downloadable assets

## Adding New QR Codes

To add additional QR codes to the project:

1. Edit `generate_qr_codes.py` and add a new entry to `QR_DESTINATIONS`:

```python
'new_qr_code': {
    'url': 'https://example.com/new-destination',
    'description': 'Description of the new QR code',
    'filename': 'new_qr_code_filename'
}
```

2. Run the generator script to create the new QR code
3. The new QR code will be automatically included in the summary report

## Troubleshooting

### QR Code Not Scanning

- **Increase size**: Make the QR code larger
- **Improve contrast**: Ensure black-on-white with good print quality
- **Check lighting**: Scan in better lighting conditions
- **Clean the lens**: Clean the smartphone camera lens

### URL Not Loading

- **Check internet connection**: Ensure device has internet access
- **Verify URL**: Manually enter the URL in a browser to test
- **Check HTTPS**: Ensure destination uses HTTPS (more secure)
- **Test on different networks**: Try cellular data vs. Wi-Fi

### Wrong Destination

- **Verify QR code file**: Ensure you're using the correct QR code file
- **Check redirects**: If using redirects, verify they're configured correctly
- **Clear cache**: Clear browser cache on the scanning device

## Support and Contact

For technical support or questions about QR code updates:

- Repository Issues: https://github.com/ELMOURABEA/Activbot/issues
- Documentation: See README.md in the project root

## Version History

- **v1.0** (2025-11-01): Initial QR code generation system with 6 destinations
  - Abu Dhabi emirate page
  - Dubai emirate page
  - Falcon eye cultural page
  - Project web page
  - Documentation page
  - 3D model downloads

---

**Note**: Always keep a backup of the original QR code generator script and generated images before making changes.
