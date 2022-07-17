import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import dataset
from torchvision.transforms import ToTensor

def download_dataset():
    train_data = dataset.MNIST(
        root = "data",
        download = True,
        train = True,
        transform = ToTensor()
    )