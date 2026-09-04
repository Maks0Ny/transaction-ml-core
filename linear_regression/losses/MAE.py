import numpy as np

class MAE:
    
    def forward(self, y_true, y_pred):
        return np.mean(abs(y_true - y_pred))
    
    def gradient(self, y_true, y_pred):
        n = len(y_true)
        return ()
        
    