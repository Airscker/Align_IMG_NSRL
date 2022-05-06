#@Author:Yufeng Wang
#@date:2022-5-6
#@Project Manual:https://airscker.github.io/Align_IMG_NSRL/
#@Copyright(C)Yufeng wang(Airscker), 2022
#@License:GPL V3.0
import cv2
import numpy as np
import os
from tqdm import tqdm
import click
@click.command()
@click.option('--path',default='images',help='The root path of images folder')
@click.option('--out_folder',default='Aligned images',help='The folder saving aligned images')
@click.option('--out_video',default='out',help='The video of aligned images,saved as name_fps.avi')
@click.option('--fps',default=60,help='The frames per second of the video')
def Img_Align(path,out_folder,out_video,fps):
    try:
        os.mkdir(out_folder)
    except:
        pass
    # Read the images to be aligned
    imgs=os.listdir(path)
    # print(imgs)
    im1 =  cv2.imread(os.path.join(path,imgs[0]),cv2.IMREAD_COLOR)
    cv2.imwrite(os.path.join(out_folder,imgs[0]),im1)
    # Convert images to grayscale
    im1_gray = cv2.cvtColor(im1,cv2.COLOR_BGR2GRAY)
    # Find size of image1
    sz = im1.shape
    #save video
    img_array=[im1]
    bar=tqdm(range(len(imgs)))
    for i in bar:
        bar.set_description('Aligning and saving {}\' image'.format(i))
        if i==0:
            pass
        else:
            im2 = cv2.imread(os.path.join(path,imgs[i]),cv2.IMREAD_COLOR)
            im2_gray = cv2.cvtColor(im2,cv2.COLOR_BGR2GRAY)
            # Define the motion model
            warp_mode = cv2.MOTION_TRANSLATION
            # Define 2x3 or 3x3 matrices and initialize the matrix to identity
            if warp_mode == cv2.MOTION_HOMOGRAPHY :
                warp_matrix = np.eye(3, 3, dtype=np.float32)
            else :
                warp_matrix = np.eye(2, 3, dtype=np.float32)
                # Specify the number of iterations.
                number_of_iterations = 5000

                # Specify the threshold of the increment
                # in the correlation coefficient between two iterations
                termination_eps = 1e-10

                # Define termination criteria
                criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, number_of_iterations,  termination_eps)

                # Run the ECC algorithm. The results are stored in warp_matrix.
                (cc, warp_matrix) = cv2.findTransformECC (im1_gray,im2_gray,warp_matrix, warp_mode, criteria)

                if warp_mode == cv2.MOTION_HOMOGRAPHY :
                    # Use warpPerspective for Homography
                    im2_aligned = cv2.warpPerspective (im2, warp_matrix, (sz[1],sz[0]), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)
                else :
                    # Use warpAffine for Translation, Euclidean and Affine
                    im2_aligned = cv2.warpAffine(im2, warp_matrix, (sz[1],sz[0]), flags=cv2.INTER_LINEAR + cv2.WARP_INVERSE_MAP)
            img_array.append(im2_aligned)
            cv2.imwrite(os.path.join(out_folder,imgs[i]),im2_aligned)
    Save_video(img_array,out_video+'_{}.avi'.format(fps),sz,fps)
    return 0
def Save_video(imgs,path,shape,frames):
    video=cv2.VideoWriter(path,cv2.VideoWriter_fourcc('D','I','V','X'),frames,(shape[1],shape[0]))
    for i in range(len(imgs)):
        video.write(imgs[i])
    video.release()
    return path
if __name__=='__main__':
    Img_Align()