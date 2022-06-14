import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("input_nii_path", help="The path to the nifti file you want to image", type=str)
parser.add_argument("output_file_path", help="The name/path of the image file to be created", type=str)
parser.add_argument('-n', '--number_of_slices', help="OPTIONAL: the number of slices to plot, default = 5", type=int)
args = parser.parse_args()

#Set slice number
if args.number_of_slices:
    num_slices = args.number_of_slices
else:
    num_slices = 5


def make_nifti_plot(input_nii_path, output_file_path, number_of_slices = 5):
    '''Function to plot sagittal slices of nifti file
    
    This function takes an input nifti, breaks it up into
    a specified number of slices, plots those slices,
    and then saves the output to output_file_path.
    
    Params
    ------
    
    input_nii_path : string
        Path to nifti file
    output_file_path : string
        Path to file that will have the figure
    number_of_slices : int, default 5
        Number of slices to display in figure
        
    Returns
    -------
    
    None - saves output to output_file_path
    
    '''
    
    nii_img = nib.load(input_nii_path) #load image
    data = nii_img.get_fdata() #grab data
    
    plt.figure(dpi = 200) # make figure
    for i in range(number_of_slices): #iterate through slices

        plt.subplot(1, number_of_slices, i + 1) #create current subplot
        slice_ind = int(np.floor(data.shape[0]/(number_of_slices + 1)*(i + 1))) #find ind for current slice
        slice_content = np.rot90(data[slice_ind,:,:].squeeze()) #grab/format slice content
        plt.imshow(slice_content) #plot slice
        plt.title('Slice Index = ' + str(slice_ind), fontsize = 'x-small') #make title
        plt.xticks([]) #get rid of ticks
        plt.yticks([])

    plt.tight_layout() #clean up the figure
    plt.savefig(output_file_path) #save the figure
    plt.close() #close the figure
    
    return
    
make_nifti_plot(args.input_nii_path, args.output_file_path, num_slices)

