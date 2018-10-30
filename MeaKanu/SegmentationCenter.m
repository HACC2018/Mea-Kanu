function SegmentationCenter(foldername,filename)

%%%% MeaKanu - Segmentation %%%%
% Jonas Krause
% krausej@hawaii.edu

%% Folders and Files
currentpath = fullfile('D:\MeaKanu\00-TEST-IMAGE\',foldername);
addpath (currentpath);
im = imread(filename);

%% IMPORTANT: cropim is the size of the TILES
cropim = 224;
[imy,imx,imz] = size(im);

% %% PATHS
pathPlant = fullfile('D:\MeaKanu\01-SEGMENTATION\plant',foldername);

%% Create Plant Mask Plant
countPlant = 0;

maxTile = min(imy,imx);

if (countPlant == 0)
    xCentPlant = int16(imx/2);
    yCentPlant = int16(imy/2);  

    if xCentPlant < cropim/2
        xCentPlant = cropim/2;
    elseif xCentPlant > imx - cropim/2
        xCentPlant = imx - cropim/2;
    end

    if yCentPlant < cropim/2
        yCentPlant = cropim/2;
    elseif yCentPlant > imy - cropim/2
        yCentPlant = imy - cropim/2;
    end 

    xmin = round(xCentPlant - cropim/2);
    ymin = round(yCentPlant - cropim/2);

    %%% EXTRACT TILES
    %%% multi-scale TILES

    fracTile = round((maxTile - cropim) / 6); % IMPORTANT: 2 x number of multi-scale tiles (left and right)

    for k = 1:3 % Number of multi-scale tiles

        xminc(k) = xmin - k*fracTile;
        yminc(k) = ymin - k*fracTile;

        if (xminc(k) + 2*k*fracTile + cropim) > imx
            xminc(k) = imx - (cropim + 2*k*fracTile);
        end

        if (yminc(k) + 2*k*fracTile + cropim) > imy
            yminc(k) = imy - (cropim + 2*k*fracTile);
        end

        if xminc(k) < 0
            xminc(k) = 0;
        end

        if yminc(k) < 0
            yminc(k) = 0;
        end

        cropsize = cropim + 2*k*fracTile;
        impc = imcrop(im,[xminc(k) yminc(k) cropsize cropsize]);
        impc = imresize(impc,[cropim cropim]);

        imwrite(impc, strcat(fullfile(pathPlant, [filename(1:end-4),sprintf('_%d.jpg',k)])));

    end

end


end


    


