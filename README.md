# Manual of Image Alignment Script

## Usage

### Step1
Let's have a glance of the steps to align the images:
- Before we start, we need to enter the root path of `alignment.py`(such as "E:\OneDrive - USTC\NSRL\Image")

![alt Root path](https://github.com/Airscker/Align_IMG_NSRL/blob/main/src/cmd.jpg?raw=true)

- First, find the root path of the folder containing images(such as "E:\OneDrive - USTC\NSRL\Image\images")
- Second, specify the path of the out_folder(such as "E:\OneDrive - USTC\NSRL\Image\Aligned images")
- Third, specify the path of the output video(such as "E:\OneDrive - USTC\NSRL\Image\out")
- Finally, specify the fps of the output video(such as 60)

### Step2
Now you can run script `alignment.py` using all the parameters in this way:

```Shell
python alignment.py --path="E:\OneDrive - USTC\NSRL\Image\images" --out_folder="E:\OneDrive - USTC\NSRL\Image\Aligned images" --out_video="E:\OneDrive - USTC\NSRL\Image\out" --fps=60
```

![alt run](https://github.com/Airscker/Align_IMG_NSRL/blob/main/src/run.jpg?raw=true)

Press Enter, then it should looks like this:

![alt go](https://github.com/Airscker/Align_IMG_NSRL/blob/main/src/go.jpg?raw=true)

After running script, you can find the results in the paths you have specified before.

### Tip

If you don't want to type in so much commands as Step2 did, you just need to put your image folder and script `alignment.py`
 under the same path such as this:

![alt Same root path](https://github.com/Airscker/Align_IMG_NSRL/blob/main/src/root.jpg?raw=true)

Then you just need to run the script as this:
```shell
python alignment.py
```
Then the images aligned will be saved in folder "Aligned images",the video will be "out_60.avi", just like this:

![alt end](https://github.com/Airscker/Align_IMG_NSRL/blob/main/src/end.jpg?raw=true)

## Parameters

| **Parameter**  | **Default**      | **Help**                                          | **Note**                                                                                                                                            |
|----------------|------------------|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `--path`       | "images"         | The root path of images folder                    | You can specify the path such as "E:\NSRL\Image\images", default path as "images" means that `alignment.py` script is in the same root path with images folder |
| `--out_folder` | "Aligned images" | The folder saving aligned images                  | Same as above                                                                                                                                       |
| `--out_video`  | "out"            | The video of aligned images,saved as name_fps.avi | Same as above(such as "E:\NSRL\Image\out")                                                                                                          |
| `--fps`        | 60               | The frames per second of the video                |                                                                                                                                                     |
