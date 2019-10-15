
# Rectangle Coordinates generation using LSTM

Implementation and visualization of a sequence generation problem formulated for generation of rectangle using LSTM.

## Model Implementation

Here we are going to use a very simple stacked model of LSTM followed by a Dense layer. Since the ouput of LSTM is 2D and input is 3D , 
so return_sequences is set to True in order to stack two LSTM layers. The model is optimized using "adam" optimizer and loss is calculated
using mean_absolute_error

## Running the model

The model is fitted on different set of example data set. I have used example set = [100,500,1000,1500,10000,20000,30000].


### Visualization of result from trained model on different set of datasets

1. Visualization of result on 100 set of examples

![100_sample_image](https://user-images.githubusercontent.com/31988698/66862039-bfeef500-efad-11e9-8516-7653580236c6.png)


2. Visualization of result on 500 set of examples

![500_sample_image](https://user-images.githubusercontent.com/31988698/66862092-da28d300-efad-11e9-988f-e5172cace5d9.png)

3. Visualization of result on 1000 set of examples

![1000_sample_image](https://user-images.githubusercontent.com/31988698/66862093-da28d300-efad-11e9-8759-7e305901b3c0.png)

4. Visualization of result on 1500 set of examples

![1500_sample_image](https://user-images.githubusercontent.com/31988698/66862095-da28d300-efad-11e9-917a-b4b9cc81835f.png)

5. Visualization of result on 10000 set of examples

![10000_sample_image](https://user-images.githubusercontent.com/31988698/66862096-dac16980-efad-11e9-9dd9-9eaaef62b200.png)


6. Visualization of result on 20000 set of examples

![20000_sample_image](https://user-images.githubusercontent.com/31988698/66862096-dac16980-efad-11e9-9dd9-9eaaef62b200.png)

7. Visualization of result on 30000 set of examples

![30000_sample_image](https://user-images.githubusercontent.com/31988698/66862096-dac16980-efad-11e9-9dd9-9eaaef62b200.png)