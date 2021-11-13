# food v2 , 데이터 정제하였음.

# inceoption resnet v2
## ft_base
block8_5_mixed ~ trainable = True  
inception resnet v2 + Flatten() + Dense(35, activation='softmax')  
batch_size = 100
epoch = 20  

### top validation accuracy model
epoch - accuracy  
15 - 0.73600

## ft_base_aug
block8_5_mixed ~ trainable = True  
inception resnet v2 + Flatten() + Dense(35, activation='softmax')  
batch_size = 100  
data augmentation
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
epoch = 50  

### top validation accuracy model
epoch - accuracy  
41 - 0.78171

## ft_base_aug
trainable = True  
inception resnet v2 + Flatten() + Dense(35, activation='softmax')  
batch_size = 50  
epoch = 50  

### top validation accuracy model
epoch - accuracy  
32 - 0.71486
