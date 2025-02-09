
import torch
import torch.nn as nn

class SimpleCNN(nn.Module):
    def __init__(self, num_classes=10):
        self.conv1 = self.make_block(3, 16, 3)
        self.conv2 = self.make_block(16, 32, 3)
        self.conv3 = self.make_block(32, 64, 3)
        self.conv4 = self.make_block(64, 128, 3)
        self.conv5 = self.make_block(128, 256, 3)
        self.fc1 = nn.Sequential(
            nn.Dropout(p=0.5),
            nn.Linear(in_features=12544, out_features=2048),
            nn.ReLU()
        )
        self.fc2 = nn.Sequential(
            nn.Dropout(p=0.5),
            nn.Linear(in_features=2048, out_features=1024),
            nn.ReLU(),
        )
        self.fc3 = nn.Linear(in_features=1024, out_features=num_classes)
    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = self.conv3(x)
        x = self.conv4(x)
        x = self.conv5(x)

        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
    def make_block(self, in_channels, out_channels, kernel_size=3):
        return nn.Sequential(
            nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=kernel_size, padding="same"),
            nn.BatchNorm2d(num_features=out_channels),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2, stride=2)
        )


if __name__ == '__main__':
