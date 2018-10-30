%%%%%%% MeaKanu %%%%%%
% Jonas Krause       %
% krausej@hawaii.edu %
%%%%%%%%%%%%%%%%%%%%%%

% Read Files on 00-TEST-IMAGE\folders %%
ImagesPaths = dir('D:\MeaKanu\00-TEST-IMAGE\*');

if size(ImagesPaths,1)>2    
    ImagesPaths(1)=[];
    ImagesPaths(1)=[];

    for i = 1:size(ImagesPaths,1) % Set how may subfolders
      
        ImagesSubPaths = fullfile('D:\MeaKanu\00-TEST-IMAGE\',ImagesPaths(i).name,'\*');
        ImagesFiles = dir(ImagesSubPaths);
        foldername = ImagesPaths(i).name;
        
        if size(ImagesFiles,1)>2
            ImagesFiles(1)=[];
            ImagesFiles(1)=[];
            
            MKCommand = ['mkdir D:\MeaKanu\01-SEGMENTATION\plant\',foldername];
            system(MKCommand);     
 
            for j = 1:size(ImagesFiles,1)
                
                filename = ImagesFiles(j).name;

                SegmentationCenter(foldername,filename);          
            end
            
            GCCommand = ['python D:\MeaKanu\03-CLASSIFICATION\ClassificationOutputTop5andTiles.py'];
            system(GCCommand);  
            
        else
            fprintf('No IMAGE on folder 1mages-%s', foldername);
            fprintf('\n');
        end    
        
    end
    
else
    fprintf('No CLASS folders under 1mages');
    fprintf('\n');
end
