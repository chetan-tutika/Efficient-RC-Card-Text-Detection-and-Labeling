# Efficient-RC-Card-Text-Detection-and-Labelling
Using tesseract for detecting words from image is a very common and very faulty without any processing. I wanted to design an algorithm to increase the efficiency of the words recognized by passing through various steps of processing before sending the image through tesseract for character recognition and labelling.

## Results
### Input Image
![rc](https://user-images.githubusercontent.com/41950483/46587284-f79c9600-ca57-11e8-8fce-597a42154d65.jpg)

### Mask for Keys
keys include: [Regn. Number’, ‘Vehicle Class’, ‘Address’, ‘Fuel Used’, ‘Regd. Owner’, ‘Type of Body’, ‘Mth. Yr. of Mfg’, ‘Maker‘s Class']
image
### Mask for Values
Includes the masked region where the values of keys are present
image
### Keys with Bounding Boxes
image
### Key Values with Bounding Boxes
image

## Final Output
The final Output is a key value pair dictionary of the relevant text in the image

## Conclusion
While the text detected is not 100% accurate, it is much better than running pytesseract on the image.
The accuracy of the output can be improved by using a better quality image or using CNN to detect text
