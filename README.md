# Scale and convert images using PIL
It's really energy and time saving if you are able to use the pillow or PIL package when dealing with a bunch of image editing.

PIL has given us the chance to kill million birds with one stone.
With PIL we can;

1. Create thumbnails
2. Rotate images
3. Change image color and a lot more.

But in this code our main aim is to rotate, resize, change images extension from .TIFF to .JPEG and save images in a new directory.

NOTE: the required output format results in black images because the source
.TIFF files have transparent background which original JPG format doesn't
support. PNG would have being more suitable option, but remember the lab calls for JPEG.
