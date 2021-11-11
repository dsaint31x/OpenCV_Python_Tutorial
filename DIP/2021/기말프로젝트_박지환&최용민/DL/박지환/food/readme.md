# food classification
# inceoption resnet v2
## main_base
inception trainable = False  
inception resnet v2 + Flatten() + Dense(35, activation='softmax')  
epoch = 20  

### top validation accuracy model
epoch - accuracy  
18 - 0.59257

## main_base2
inception trainable = False  
inception resnet v2 + Flatten() + Dense(256, activation='relu') + Dense(35, activation='softmax')  
epoch = 20

### top validation accuracy model
epoch - accuracy  
13 - 0.59200

## main_finetuning_base
inception trainable (block8_1_mixed ~) = True  
inception resnet v2 + Flatten() + Dense(35, activation='softmax')  
epoch = 20

### top validation accuracy model
epoch - accuracy  
19 - 0.67714

## main_finetuning_base2
inception trainable (block8_5_mixed ~) = True  
inception resnet v2 + Flatten() + Dense(35, activation='softmax')  
epoch = 100

### top validation accuracy model
epoch - accuracy  
52 - 0.68514

## main_finetuning_base2_drop
inception trainable (block8_5_mixed ~) = True  
inception resnet v2 + Flatten() + Dropout(0.5) + Dense(35, activation='softmax')  
epoch = 100

### top validation accuracy model
epoch - accuracy  
16 - 0.69200

## main_finetuning_dense
inception trainable (block8_5_mixed ~) = True  
inception resnet v2 + Flatten() + Dense(256, activation='relu') + Dense(35, activation='softmax')  
epoch = 20

### top validation accuracy model
epoch - accuracy  
05 - 0.67714

## main_finetuning_dense_drop
inception trainable (block8_5_mixed ~) = True 
batchsize = 100
inception resnet v2 + Flatten() + Dropout(0.5) + Dense(35, activation='softmax')  
epoch = 100

### top validation accuracy model
epoch - accuracy  
61 - 0.69829

## main_finetuning_base2_drop_augmentation
inception trainable (block8_5_mixed ~) = True 
batchsize = 100
image augmentation 
```python
data_gen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=100,
    width_shift_range=0.4,
    height_shift_range=0.4,
    horizontal_flip=True,
    zoom_range=0.2,
    shear_range=0.2
)
```
inception resnet v2 + Flatten() + Dropout(0.5) + Dense(35, activation='softmax')  
epoch = 100

### top validation accuracy model
epoch - accuracy  
61 - 0.69829

--------------
# ResNet
## main_resnet50
ResNet50 trainable = False  
ResNet50 + Flatten() + Dense(35, activation='softmax')  
epoch = 20

### top validation accuracy model
epoch - accuracy  
80 - 0.74857

## main_resnet50_finetuning
ResNet50 trainable (conv5_block1_1_conv ~) = True  
ResNet50 + Flatten() + Dense(35, activation='softmax')  
epoch = 20

### top validation accuracy model
epoch - accuracy  
17 - 0.18457

## main_resnet101_finetuning
ResNet101 trainable (conv5_block1_1_conv ~) = True  
ResNet101 + Flatten() + Dense(35, activation='softmax')  
epoch = 40

### top validation accuracy model
epoch - accuracy  
33 - 0.19200
