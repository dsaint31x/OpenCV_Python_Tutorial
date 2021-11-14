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

## ft_x
trainable = True  
inception resnet v2 + Flatten() + Dense(35, activation='softmax')  
batch_size = 50  
epoch = 50  

### top validation accuracy model
epoch - accuracy  
32 - 0.71486

## ft_x_aug
trainable = True  
inception resnet v2 + Flatten() + Dense(35, activation='softmax')  
batch_size = 50  
data augmentation
epoch = 50  

### top validation accuracy model
epoch - accuracy  
29 - 0.78057

## ft_base_aug_lr
block8_5_mixed ~ trainable = True  
inception resnet v2 + Flatten() + Dense(35, activation='softmax')  
batch_size = 100  
data augmentation  
learning rate decay  
epoch = 50  

### top validation accuracy model
epoch - accuracy  
26 - 0.80286

## ft_gap_aug_lr
block8_5_mixed ~ trainable = True  
inception resnet v2 + GlobalAveragePooling2D() + Dense(35, activation='softmax')  
batch_size = 100  
data augmentation  
learning rate decay  
epoch = 50  

### top validation accuracy model
epoch - accuracy  
25 - 0.80914

## ft_gap_aug_lr_299
block8_5_mixed ~ trainable = True  
inception resnet v2 + GlobalAveragePooling2D() + Dense(35, activation='softmax')  
batch_size = 100  
data augmentation  
learning rate decay  
input_size = (299,299)  
epoch = 50  

### top validation accuracy model
epoch - accuracy  
37 - 0.86800
