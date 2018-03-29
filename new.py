def get_an_internet_image(url):
    if not url:
        return

    try:
        # Prefix with 'file://' for local file.
        if os.path.exists(url):
            url = 'file://' + url
        f = urllib.request.urlopen(url)
        jpeg_str = f.read()
    except IOError:
        print(( 'invalid url: ' + url))
        return

    orignal_im = Image.open(StringIO.StringIO(jpeg_str))
    print(( 'running deeplab on image %s...' % url))
    resized_im, seg_map = model.run(orignal_im)