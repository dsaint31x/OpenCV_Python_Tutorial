# food classification

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
