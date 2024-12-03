this project aims to crop xpm images
here is an example:

BEFORE :

![Screenshot from 2024-12-03 18-36-50](https://github.com/user-attachments/assets/0def61db-9dad-43fb-a890-c3ae9c114b5e)

AFTER :

![Screenshot from 2024-12-03 18-38-11](https://github.com/user-attachments/assets/67e51b68-b7c8-4528-ba3d-ebb533913f74)

In our project, we use XPM images with the MiniLibX graphical library. Since MiniLibX doesn't handle invisible pixels,
every pixel must be checked before being drawn.
By cropping the image, we can significantly reduce the time required for this process, making it more efficient.
