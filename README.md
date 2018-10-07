# Efficient-RC-Card-Text-Detection-and-Labelling
Using tesseract for detecting words from image is a very common and very faulty without any processing. I wanted to design an algorithm to increase the efficiency of the words recognized by passing through various steps of processing before sending the image through tesseract for character recognition and labelling.

## Results
### Input Image
![rc](https://user-images.githubusercontent.com/41950483/46587284-f79c9600-ca57-11e8-8fce-597a42154d65.jpg)

### Mask for Keys
keys include: [Regn. Number’, ‘Vehicle Class’, ‘Address’, ‘Fuel Used’, ‘Regd. Owner’, ‘Type of Body’, ‘Mth. Yr. of Mfg’, ‘Maker‘s Class']
![keys](https://user-images.githubusercontent.com/41950483/46587355-53b3ea00-ca59-11e8-859e-d664ea6ba383.png)
### Mask for Values
Includes the masked region where the values of keys are present
![values](https://user-images.githubusercontent.com/41950483/46587366-70e8b880-ca59-11e8-8f88-db565967174a.png)
### Keys with Bounding Boxes
![keys1](https://user-images.githubusercontent.com/41950483/46587384-bf965280-ca59-11e8-86a4-c3cdab5e5d28.png)
### Key Values with Bounding Boxes
![values1](https://user-images.githubusercontent.com/41950483/46587391-d9379a00-ca59-11e8-8c81-18e7932e06d1.png)
## Final Output
The final Output is a key value pair dictionary of the relevant text in the image
{‘Regn. Number’: ‘AP16CF9628’, ‘Vehicle Cliass’: ‘MOTOR CYCLE’, ‘Address’: ‘8—198/2 PLOT NO 306 GAYATRI RFS BLOCK MAIN ROAD KANURU’, ‘Fuel Used’: ‘PETROL’, ‘Regd. Owner’: ‘K RAVI VARMA NAGESWARA RAG’, ‘Type of Body’: ‘SOLO’, ‘Mth. Yr. of Mfg’: ‘22013’, ‘Maker‘s Class’: ‘PULSAR 150 DTS— BSill’}
## Conclusion
While the text detected is not 100% accurate, it is much better than running pytesseract on the image.
The accuracy of the output can be improved by using a better quality image or using CNN to detect text
