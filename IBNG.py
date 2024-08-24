from tkinter import Label, Button, Tk, filedialog, ttk, Scrollbar, Frame, Canvas, Text, font, Entry, colorchooser
from tkinter.messagebox import showwarning
from ttkthemes import ThemedStyle
from PIL import Image, ImageDraw, ImageFont, ImageTk, ImageGrab
from tkinterdnd2 import DND_FILES, TkinterDnD
import time
import threading
import traceback
import numpy as np
import os
from os import listdir
from os.path import isfile, join
import math
from collections import Counter, deque
import cv2
import sys
import numpy as np
import matplotlib.font_manager
import ctypes
import shutil
import ast



ContourModeNumber=3


def GetDataFilePath(RelativePath):
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, RelativePath) if hasattr(sys, '_MEIPASS') else os.path.abspath(".")
    elif __file__:
        return ApplicationPath+'/'+RelativePath


if getattr(sys, 'frozen', False):
    ApplicationPath = str(os.path.dirname(sys.executable))
elif __file__:
    ApplicationPath = str(os.path.dirname(__file__))

print(ApplicationPath)













def IBNGExcepthook():
    showwarning("Unhandled Exception", f"Sorry something went wrong: {sys.exc_info()}")
    
    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
    [IBNGWindow.unbind_all(Event) for Event in Bindings]
    [IBNGWindow.unbind(Event) for Event in Bindings]


    IBNGWindow.after(100, OpenMainWindow)

sys.excepthook = IBNGExcepthook



Bindings = ["<Up>", '<Down>', '<Right>', '<Left>','<Button-1>', '<B1-Motion>', '<ButtonRelease-1>', '<Double-Button-1>', '<Enter>', '<Leave>', '<FocusIn>', '<FocusOut>', '<Return>', '<Shift-Up>', '<Configure>', '<MouseWheel>', '<Shift-MouseWheel>']


if not os.path.exists(ApplicationPath+'/Cash'):
    os.makedirs(ApplicationPath+'/Cash')
if not os.path.exists(ApplicationPath+'/Cash/ResultsFiles'):
   os.makedirs(ApplicationPath+'/Cash/ResultsFiles')
if not os.path.exists(ApplicationPath+'/Cash/SystemLanguage.txt'):
   open(ApplicationPath+'/Cash/SystemLanguage.txt', 'w').write('English')
if not os.path.exists(ApplicationPath+'/Cash/DownloadFileFormat.txt'):
   open(ApplicationPath+'/Cash/DownloadFileFormat.txt', 'w').write('.png')
if not os.path.exists(ApplicationPath+'/Cash/StockColorsSet.txt'):
   open(ApplicationPath+'/Cash/StockColorsSet.txt', 'w').write('System')
if not os.path.exists(ApplicationPath+'/Cash/StockColorsSets.txt'):
   open(ApplicationPath+'/Cash/StockColorsSets.txt', 'w').write('System:[(56, 6, 91), (156, 189, 228), (97, 193, 215), (123, 79, 142), (101, 81, 166), (68, 0, 50), (118, 120, 124), (254, 233, 177), (111, 156, 186), (0, 128, 198), (250, 240, 143), (254, 240, 82), (255, 227, 41), (25, 53, 154), (96, 210, 216), (255, 183, 0), (255, 100, 20), (255, 52, 27), (0, 194, 183), (148, 217, 183), (255, 33, 31), (214, 13, 24), (182, 2, 40), (187, 223, 143), (0, 165, 67), (255, 74, 107), (255, 170, 155), (255, 179, 205), (0, 71, 15), (138, 177, 143), (239, 183, 215), (243, 157, 200), (250, 165, 202), (184, 163, 163), (164, 97, 27), (255, 54, 117), (183, 0, 72), (197, 148, 199), (149, 28, 3), (63, 24, 0), (114, 135, 142), (255, 255, 255), (0, 185, 232), (3, 1, 69), (0, 104, 135), (0, 186, 56), (0, 68, 29), (195, 134, 28), (100, 79, 61)]')


class Times():
   global StartTime
   def start():
      global StartTime
      StartTime=time.time()
   def stop():
      print(time.time()-StartTime)





    

IBNGWindow=TkinterDnD.Tk()




def UploadResources():
    global SystemLanguage, DownloadFileFormat, StockColorsSetName, StockColorsSets, ColorsStock, ImagesInformationEnglish, PillowImagesEnglish, TkImagesEnglish, WidgetsInformationEnglish, WidgetsEnglish, ImagesInformationUkrainian, PillowImagesUkrainian, TkImagesUkrainian, WidgetsInformationUkrainian, WidgetsUkrainian,  PillowImages, TkImages, WidgetsInformation,  Widgets, PillowButtonContourImages, TkButtonContourImages, PillowButtonContourImageSettingsClamped, TkButtonContourImageSettingsClamped, PillowButtonContourImageConfigureContourImage, TkButtonContourImageConfigureContourImage, CreatedImages
    def GetPillowImageEnglish(FileName, Size):
       if Size != (0, 0):
          return Image.open(GetDataFilePath('English/'+FileName)).resize(Size)
       else:
          return Image.open(GetDataFilePath('English/'+FileName))



    def GetPillowImageUkrainian(FileName, Size):
       if Size != (0, 0):
          return Image.open(GetDataFilePath('Ukrainian/'+FileName)).resize(Size)
       else:
          return Image.open(GetDataFilePath('Ukrainian/'+FileName))




    SystemLanguage=str(open(ApplicationPath+'/Cash/SystemLanguage.txt', 'r').read())
    DownloadFileFormat=str(open(ApplicationPath+'/Cash/DownloadFileFormat.txt', 'r').read())
    StockColorsSetName=str(open(ApplicationPath+'/Cash/StockColorsSet.txt', 'r').read())

    StockColorsSets=str(open(ApplicationPath+'/Cash/StockColorsSets.txt', 'r').read())
    for StockColorsSet in StockColorsSets.split('\n'):
        if StockColorsSetName in StockColorsSet:
            ColorsStock=ast.literal_eval(StockColorsSet[StockColorsSet.find(':')+1:])
            break  








    #English

    ImagesInformationEnglish = [
        ('BackgroundDetail1.png', (4000, 71)),
        ('BackgroundDetail1ConfigureContourImage.png', (4000, 71)),
        ('BackgroundDetail2.png', (4000, 111)),
        ('BackgroundDetail2ConfigureContourImage.png', (4000, 111)),
        ('BackgroundDetail3.png', (4000, 97)),
        ('BackgroundDetail4.png', (4000, 126)),
        ('BackgroundDetail5.png', (4000, 150)),
        ('IBNGTextIcon.png', (196, 64)),
        ('IBNGTextIconConfigureContourImage.png', (196, 64)),
        ('ProcessFilePlace.png', (0, 0)),
        ('YourContentText.png', (0, 0)),
        ('YourContentTextConfigureContourImage.png', (0, 0)),
        ('AllCreationsHereText.png', (0, 0)),
        ('SettingsText.png', (0, 0)),
        ('LanguageText.png', (0, 0)),
        ('ModeFirstTip.png', (0, 0)),
        ('ModeSecondTip.png', (0, 0)),
        ('ModeThirdTip.png', (0, 0)),
        ('ChooseContourModeText.png', (0, 0)),
        ('InstractionText.png', (0, 0)),
        ('SelectAnImageText.png', (0, 0)),
        ('SelectAContourText.png', (0, 0)),
        ('ImageProcessingText.png', (0, 0)),
        ('RealColorsText.png', (0, 0)),
        ('ExpectedColorsText.png', (0, 0)),
        ('PromptText.png', (0, 0)),
        ('ProcessText.png', (0, 0)),
        ('ImageStatisticsCreatedText.png', (0, 0)),
        ('PaletteCreatedText.png', (0, 0)),
        ('ImageByNumberCreatedText.png', (0, 0)),
        ('StockImageColorCreatedText.png', (0, 0)),
        ('ImageStatisticsResultFileText.png', (0, 0)),
        ('PaletteResultFileText.png', (0, 0)),
        ('ImageByNumberResultFileText.png', (0, 0)),
        ('StockImageColorResultFileText.png', (0, 0)),
        ('SelectColorsFromStockText.png', (0, 0)),
        ('ChooseColorsFromStockText.png', (0, 0)),
        ('ThisPageIsNotAvailableYet.png', (0, 0)),
        ('TextFileResultFileIcon.png', (0, 0)),
        ('PaletteResultFileIcon.png', (0, 0)),
        ('ImageByNumberResultFileIcon.png', (0, 0)),
        ('ImageByColorFromStockResultFileIcon.png', (0, 0)),
        ('TextFileIcon.png', (0, 0)),
        ('PaletteCreateIcon.png', (0, 0)),
        ('ImageByNumberIcon.png', (0, 0)),
        ('ImageByColorFromStockIcon.png', (0, 0)),
        ('SettingsCheckMark.png', (0, 0)),
        ('ExportSettingsPlaceButtonRealesed.png', (0, 0)),
        ('ExportSettingsPlaceButtonPngClamped.png', (0, 0)),
        ('ExportSettingsPlaceButtonJpgClamped.png', (0, 0)),
        ('ExportSettingsPlaceButtonJpegClamped.png', (0, 0)),
        ('PriorityLanguageSettingsPlaceButtonRealesed.png', (0, 0)),
        ('PriorityLanguageSettingsPlaceButtonClamped.png', (0, 0)),
        ('LanguageSettingsPlaceButtonRealesed.png', (0, 0)),
        ('LanguageSettingsPlaceButtonEnglishClamped.png', (0, 0)),
        ('LanguageSettingsPlaceButtonUkrainianClamped.png', (0, 0)),
        ('ColorSetsSettingsPlaceButtonRealesed.png', (0, 0)),
        ('ColorSetsSettingsPlaceButtonClamped.png', (0, 0)),
        ('ColorSetsText.png', (0, 0)),
        ('ColorSetSettingsPlaceButtonClamped.png', (0, 0)),
        ('ColorSetSettingsPlaceButtonRealesed.png', (0, 0)),
        ('ColorSetSettingsPlaceButtonUsed.png', (0, 0)),
        ('ColorSetSettingsPlaceButtonUsedClamped.png', (0, 0)),
        ('AddColorSetSettingsPlaceButtonRealesed.png', (0, 0)),
        ('AddColorSetSettingsPlaceButtonClamped.png', (0, 0)), 
        ('PaletteAddColorDeleteButtonRealesed.png', (0, 0)),
        ('PaletteAddColorDeleteButtonClamped.png', (0, 0)),
        ('PaletteAddColorClamped.png', (0, 0)),
        ('AddColorPaletteRealesed.png', (80, 80)),
        ('AddColorPaletteClamped.png', (80, 80)),
        ('SaveColorSetRealesed.png', (0, 0)),
        ('SaveColorSetClamped.png', (0, 0)),
        ('SaveAndUseColorSetRealesed.png', (0, 0)),
        ('SaveAndUseColorSetClamped.png', (0, 0)),
        ('DeleteColorSetRealesed.png', (0, 0)),
        ('DeleteColorSetClamped.png', (0, 0)),
        ('ProcessIconPart1.png', (0, 0)),
        ('ProcessIconPart2.png', (0, 0)),
        ('ProcessIconPart3.png', (0, 0)),
        ('ProcessIconPart4.png', (0, 0)),
        ('ProcessIconPart5.png', (0, 0)),
        ('ProcessIconPart6.png', (0, 0)),
        ('ProcessIconPart7.png', (0, 0)),
        ('ProcessIconPart8.png', (0, 0)),
        ('ProcessIconPart9.png', (0, 0)),
        ('ProcessIconPart10.png', (0, 0)),
        ('ProcessIconPart11.png', (0, 0)),
        ('ProcessIconPart12.png', (0, 0)),
        ('ProcessIconPart13.png', (0, 0)),
        ('ProcessIconPart14.png', (0, 0)),
        ('ProcessIconPart15.png', (0, 0)),
        ('ProcessIconPart16.png', (0, 0)),
        ('ProcessIconPart17.png', (0, 0)),
        ('ProcessIconPart18.png', (0, 0)),
        ('ProcessIconPart19.png', (0, 0)),
        ('ProcessIconPart20.png', (0, 0)),
        ('ProcessIconPart21.png', (0, 0)),
        ('ProcessIconPart22.png', (0, 0)),
        ('ProcessIconPart23.png', (0, 0)),
        ('ProcessIconPart24.png', (0, 0)),
        ('ErrorOpenImage1.png', (0, 0)),
        ('ErrorOpenImage2.png', (0, 0)),
        ('ChooseContourModeTips.png', (0, 0)),
        ('ImageUploadedIcon.png', (0, 0)),
        ('StatisticUploadedIcon.png', (0, 0)),
        ('FirstContourModeButton.png', (0, 0)),
        ('SecondContourModeButton.png', (0, 0)),
        ('ThirdContourModeButton.png', (0, 0)),
        ('StartCreatingButtonRealesed.png', (0, 0)),
        ('SettingsButtonRealesed.png', (0, 0)),
        ('SettingsButtonConfigureContourImage.png', (0, 0)),
        ('StartCreatingButtonClamped.png', (0, 0)),
        ('StartCreatingButtonConfigureContourImage.png', (0, 0)),
        ('SettingsButtonClamped.png', (0, 0)),
        ('HomeButtonRealesed.png', (0, 0)),
        ('HomeButtonClamped.png', (0, 0)),
        ('InfoContourModeButtonRealesed.png', (0, 0)),
        ('InfoContourModeButtonClamped.png', (0, 0)),
        ('BackButtonRealesed.png', (0, 0)),
        ('BackButtonClamped.png', (0, 0)),
        ('ChooseOrDropButtonRealesed.png', (0, 0)),
        ('ChooseButtonClamped.png', (0, 0)),
        ('DropButtonClamped.png', (0, 0)),
        ('ConfirmButtonRealesed.png', (0, 0)),
        ('ConfirmButtonClamped.png', (0, 0)),
        ('ChooseAnotherImageButtonRealesed.png', (0, 0)),
        ('ChooseAnotherImageButtonClamped.png', (0, 0)),
        ('DownloadButtonRealesed.png', (0, 0)),
        ('DownloadButtonClamped.png', (0, 0)),
        ('CancelButtonRealesed.png', (0, 0)),
        ('CancelButtonClamped.png', (0, 0)),
        ('SaveButtonRealesed.png', (0, 0)),
        ('SaveButtonClamped.png', (0, 0)),
        ('RenameButtonContourImageRealesed.png', (0, 0)),
        ('RenameButtonContourImageClamped.png', (0, 0)),
        ('DeleteButtonContourImageRealesed.png', (0, 0)),
        ('DeleteButtonContourImageClamped.png', (0, 0)),
        ('ConfigureContourImageBackground.png', (0, 0)),
        ('AcceptButtonRealesed.png', (0, 0)),
        ('AcceptButtonClamped.png', (0, 0)),
        ('CancelRenameButtonRealesed.png', (0, 0)),
        ('CancelRenameButtonClamped.png', (0, 0))
    ]



    PillowImagesEnglish = {ImageInformation[0].replace('.png', ''): GetPillowImageEnglish(ImageInformation[0], ImageInformation[1]) for ImageInformation in ImagesInformationEnglish}

    TkImagesEnglish = {PillowImage[0]: ImageTk.PhotoImage(PillowImage[1]) for PillowImage in PillowImagesEnglish.items()}

    WidgetsInformationEnglish = [
        ('BackgroundDetail1', TkImagesEnglish['BackgroundDetail1'], 'fff9e9'),
        ('BackgroundDetail2', TkImagesEnglish['BackgroundDetail2'], 'fff9e9'),
        ('BackgroundDetail3', TkImagesEnglish['BackgroundDetail3'], 'fff9e9'),
        ('BackgroundDetail4', TkImagesEnglish['BackgroundDetail4'], 'fff9e9'),
        ('BackgroundDetail5', TkImagesEnglish['BackgroundDetail5'], 'fff9e9'),
        ('IBNGTextIcon', TkImagesEnglish['IBNGTextIcon'], 'fff9e9'),
        ('ProcessFilePlace1', TkImagesEnglish['ProcessFilePlace'], 'fff9e9'),
        ('ProcessFilePlace2', TkImagesEnglish['ProcessFilePlace'], 'fff9e9'),
        ('ProcessFilePlace3', TkImagesEnglish['ProcessFilePlace'], 'fff9e9'),
        ('ProcessFilePlace4', TkImagesEnglish['ProcessFilePlace'], 'fff9e9'),
        ('YourContentText', TkImagesEnglish['YourContentText'], 'fff7d9'),
        ('AllCreationsHereText', TkImagesEnglish['AllCreationsHereText'], 'fff9e9'),
        ('ModeFirstTip', TkImagesEnglish['ModeFirstTip'], 'fff9e9'),
        ('ModeSecondTip', TkImagesEnglish['ModeSecondTip'], 'fff9e9'),
        ('ModeThirdTip', TkImagesEnglish['ModeThirdTip'], 'fff9e9'),
        ('SettingsText', TkImagesEnglish['SettingsText'], 'fff7d9'),
        ('LanguageText', TkImagesEnglish['LanguageText'], 'fff7d9'),
        ('ExportSettingsPlaceButton', TkImagesEnglish['ExportSettingsPlaceButtonRealesed'], 'fff9e9'),
        ('LanguageSettingsPlaceButton', TkImagesEnglish['LanguageSettingsPlaceButtonRealesed'], 'fff9e9'),
        ('PriorityLanguageSettingsPlaceButton', TkImagesEnglish['PriorityLanguageSettingsPlaceButtonRealesed'], 'fff9e9'),
        ('ColorSetsSettingsPlaceButton', TkImagesEnglish['ColorSetsSettingsPlaceButtonRealesed'], 'fff9e9'),
        ('ChooseContourModeText', TkImagesEnglish['ChooseContourModeText'], 'fff7d9'),
        ('InstractionText', TkImagesEnglish['InstractionText'], 'fff7d9'),
        ('SelectAnImageText', TkImagesEnglish['SelectAnImageText'], 'fff7d9'),
        ('SelectAContourText', TkImagesEnglish['SelectAContourText'], 'fff7d9'),
        ('ImageProcessingText', TkImagesEnglish['ImageProcessingText'], 'fff9e9'),
        ('PromptText', TkImagesEnglish['PromptText'], 'fff9e9'),
        ('ProcessText', TkImagesEnglish['ProcessText'], 'fff7d9'),
        ('ColorSetsText', TkImagesEnglish['ColorSetsText'], 'fff7d9'),
        ('ExpectedColorsText', TkImagesEnglish['ExpectedColorsText'], 'fff9e9'),
        ('RealColorsText', TkImagesEnglish['RealColorsText'], 'fff9e9'),
        ('ImageStatisticsCreatedText', TkImagesEnglish['ImageStatisticsCreatedText'], 'fff9e9'),
        ('PaletteCreatedText', TkImagesEnglish['PaletteCreatedText'], 'fff9e9'),
        ('StockImageColorCreatedText', TkImagesEnglish['StockImageColorCreatedText'], 'fff9e9'),
        ('ImageByNumberCreatedText', TkImagesEnglish['ImageByNumberCreatedText'], 'fff9e9'),
        ('ImageStatisticsResultFileText', TkImagesEnglish['ImageStatisticsResultFileText'], 'fff9e9'),
        ('PaletteResultFileText', TkImagesEnglish['PaletteResultFileText'], 'fff9e9'),
        ('StockImageColorResultFileText', TkImagesEnglish['StockImageColorResultFileText'], 'fff9e9'),
        ('ImageByNumberResultFileText', TkImagesEnglish['ImageByNumberResultFileText'], 'fff9e9'),
        ('SelectColorsFromStockText', TkImagesEnglish['SelectColorsFromStockText'], 'fff7d9'),
        ('ChooseColorsFromStockText', TkImagesEnglish['ChooseColorsFromStockText'], 'fff7d9'),
        ('ChooseColorsFromStockText', TkImagesEnglish['ChooseColorsFromStockText'], 'fff7d9'),
        ('ThisPageIsNotAvailableYet', TkImagesEnglish['ThisPageIsNotAvailableYet'], 'fff9e9'),
        ('TextFileIcon', TkImagesEnglish['TextFileIcon'], 'fbf1ca'),
        ('PaletteCreateIcon', TkImagesEnglish['PaletteCreateIcon'], 'fbf1ca'),
        ('ImageByNumberIcon', TkImagesEnglish['ImageByNumberIcon'], 'fbf1ca'),
        ('ImageByColorFromStockIcon', TkImagesEnglish['ImageByColorFromStockIcon'], 'fbf1ca'),
        ('TextFileResultFileIcon', TkImagesEnglish['TextFileResultFileIcon'], 'fff9e9'),
        ('PaletteResultFileIcon', TkImagesEnglish['PaletteResultFileIcon'], 'fff9e9'),
        ('ImageByNumberResultFileIcon', TkImagesEnglish['ImageByNumberResultFileIcon'], 'fff9e9'),
        ('ImageByColorFromStockResultFileIcon', TkImagesEnglish['ImageByColorFromStockResultFileIcon'], 'fff9e9'),
        ('ErrorOpenImage1', TkImagesEnglish['ErrorOpenImage1'], 'fff9e9'),
        ('ErrorOpenImage2', TkImagesEnglish['ErrorOpenImage2'], 'fff9e9'),
        ('ChooseContourModeTips', TkImagesEnglish['ChooseContourModeTips'], 'fff9e9'),
        ('FirstContourModeButton', TkImagesEnglish['FirstContourModeButton'], 'fff9e9'),
        ('SecondContourModeButton', TkImagesEnglish['SecondContourModeButton'], 'fff9e9'),
        ('ThirdContourModeButton', TkImagesEnglish['ThirdContourModeButton'], 'fff9e9'),
        ('StartCreatingButton', TkImagesEnglish['StartCreatingButtonRealesed'], 'fff9e9'),
        ('ImageUploadedIcon', TkImagesEnglish['ImageUploadedIcon'], 'fff7d9'),
        ('StatisticUploadedIcon', TkImagesEnglish['StatisticUploadedIcon'], 'fff7d9'),
        ('SettingsButton', TkImagesEnglish['SettingsButtonRealesed'], 'fff9e9'),
        ('AcceptButton', TkImagesEnglish['AcceptButtonRealesed'], 'fff9e9'),
        ('CancelRenameButton', TkImagesEnglish['CancelRenameButtonRealesed'], 'fff9e9'),
        ('HomeButton', TkImagesEnglish['HomeButtonRealesed'], 'fff7d9'),
        ('DownloadButton', TkImagesEnglish['DownloadButtonRealesed'], 'fff7d9'),
        ('BackButton', TkImagesEnglish['BackButtonRealesed'], 'fff7d9'),
        ('ChooseOrDropButton', TkImagesEnglish['ChooseOrDropButtonRealesed'], 'fff9e9'),
        ('ConfirmButton', TkImagesEnglish['ConfirmButtonRealesed'], 'fff9e9'),
        ('ChooseAnotherImageButton', TkImagesEnglish['ChooseAnotherImageButtonRealesed'], 'fff9e9'),
        ('ProcessIcon', TkImagesEnglish['ProcessIconPart6'], 'fff9e9'),
        ('SaveButton', TkImagesEnglish['SaveButtonRealesed'], 'fff9e9'),
        ('CancelButton', TkImagesEnglish['CancelButtonRealesed'], 'fff7d9'),
        ('RenameButtonContourImage', TkImagesEnglish['RenameButtonContourImageRealesed'], 'fff7d9'),
        ('DeleteButtonContourImage', TkImagesEnglish['DeleteButtonContourImageRealesed'], 'fff7d9')
    ]


    WidgetsEnglish = {WidgetInformation[0]: Label(IBNGWindow, image=WidgetInformation[1], bg="#"+WidgetInformation[2], bd=0) for WidgetInformation in WidgetsInformationEnglish}







    #Ukrainian

    ImagesInformationUkrainian = [
        ('BackgroundDetail1.png', (4000, 71)),
        ('BackgroundDetail1ConfigureContourImage.png', (4000, 71)),
        ('BackgroundDetail2.png', (4000, 111)),
        ('BackgroundDetail2ConfigureContourImage.png', (4000, 111)),
        ('BackgroundDetail3.png', (4000, 97)),
        ('BackgroundDetail4.png', (4000, 126)),
        ('BackgroundDetail5.png', (4000, 150)),
        ('IBNGTextIcon.png', (196, 64)),
        ('IBNGTextIconConfigureContourImage.png', (196, 64)),
        ('ProcessFilePlace.png', (0, 0)),
        ('YourContentText.png', (0, 0)),
        ('YourContentTextConfigureContourImage.png', (0, 0)),
        ('AllCreationsHereText.png', (0, 0)),
        ('SettingsText.png', (0, 0)),
        ('LanguageText.png', (0, 0)),
        ('ModeFirstTip.png', (0, 0)),
        ('ModeSecondTip.png', (0, 0)),
        ('ModeThirdTip.png', (0, 0)),
        ('ChooseContourModeText.png', (0, 0)),
        ('InstractionText.png', (0, 0)),
        ('SelectAnImageText.png', (0, 0)),
        ('SelectAContourText.png', (0, 0)),
        ('ImageProcessingText.png', (0, 0)),
        ('RealColorsText.png', (0, 0)),
        ('ExpectedColorsText.png', (0, 0)),
        ('PromptText.png', (0, 0)),
        ('ProcessText.png', (0, 0)),
        ('ImageStatisticsCreatedText.png', (0, 0)),
        ('PaletteCreatedText.png', (0, 0)),
        ('ImageByNumberCreatedText.png', (0, 0)),
        ('StockImageColorCreatedText.png', (0, 0)),
        ('ImageStatisticsResultFileText.png', (0, 0)),
        ('PaletteResultFileText.png', (0, 0)),
        ('ImageByNumberResultFileText.png', (0, 0)),
        ('StockImageColorResultFileText.png', (0, 0)),
        ('SelectColorsFromStockText.png', (0, 0)),
        ('ChooseColorsFromStockText.png', (0, 0)),
        ('ThisPageIsNotAvailableYet.png', (0, 0)),
        ('TextFileResultFileIcon.png', (0, 0)),
        ('PaletteResultFileIcon.png', (0, 0)),
        ('ImageByNumberResultFileIcon.png', (0, 0)),
        ('ImageByColorFromStockResultFileIcon.png', (0, 0)),
        ('TextFileIcon.png', (0, 0)),
        ('PaletteCreateIcon.png', (0, 0)),
        ('ImageByNumberIcon.png', (0, 0)),
        ('ImageByColorFromStockIcon.png', (0, 0)),
        ('SettingsCheckMark.png', (0, 0)),
        ('ExportSettingsPlaceButtonRealesed.png', (0, 0)),
        ('ExportSettingsPlaceButtonPngClamped.png', (0, 0)),
        ('ExportSettingsPlaceButtonJpgClamped.png', (0, 0)),
        ('ExportSettingsPlaceButtonJpegClamped.png', (0, 0)),
        ('PriorityLanguageSettingsPlaceButtonRealesed.png', (0, 0)),
        ('PriorityLanguageSettingsPlaceButtonClamped.png', (0, 0)),
        ('LanguageSettingsPlaceButtonRealesed.png', (0, 0)),
        ('LanguageSettingsPlaceButtonEnglishClamped.png', (0, 0)),
        ('LanguageSettingsPlaceButtonUkrainianClamped.png', (0, 0)),
        ('ColorSetsSettingsPlaceButtonRealesed.png', (0, 0)),
        ('ColorSetsSettingsPlaceButtonClamped.png', (0, 0)),
        ('ColorSetsText.png', (0, 0)),
        ('ColorSetSettingsPlaceButtonClamped.png', (0, 0)),
        ('ColorSetSettingsPlaceButtonRealesed.png', (0, 0)),
        ('ColorSetSettingsPlaceButtonUsed.png', (0, 0)),
        ('ColorSetSettingsPlaceButtonUsedClamped.png', (0, 0)),
        ('AddColorSetSettingsPlaceButtonRealesed.png', (0, 0)),
        ('AddColorSetSettingsPlaceButtonClamped.png', (0, 0)), 
        ('PaletteAddColorDeleteButtonRealesed.png', (0, 0)),
        ('PaletteAddColorDeleteButtonClamped.png', (0, 0)),
        ('PaletteAddColorClamped.png', (0, 0)),
        ('AddColorPaletteRealesed.png', (80, 80)),
        ('AddColorPaletteClamped.png', (80, 80)),
        ('SaveColorSetRealesed.png', (0, 0)),
        ('SaveColorSetClamped.png', (0, 0)),
        ('SaveAndUseColorSetRealesed.png', (0, 0)),
        ('SaveAndUseColorSetClamped.png', (0, 0)),
        ('DeleteColorSetRealesed.png', (0, 0)),
        ('DeleteColorSetClamped.png', (0, 0)),
        ('ProcessIconPart1.png', (0, 0)),
        ('ProcessIconPart2.png', (0, 0)),
        ('ProcessIconPart3.png', (0, 0)),
        ('ProcessIconPart4.png', (0, 0)),
        ('ProcessIconPart5.png', (0, 0)),
        ('ProcessIconPart6.png', (0, 0)),
        ('ProcessIconPart7.png', (0, 0)),
        ('ProcessIconPart8.png', (0, 0)),
        ('ProcessIconPart9.png', (0, 0)),
        ('ProcessIconPart10.png', (0, 0)),
        ('ProcessIconPart11.png', (0, 0)),
        ('ProcessIconPart12.png', (0, 0)),
        ('ProcessIconPart13.png', (0, 0)),
        ('ProcessIconPart14.png', (0, 0)),
        ('ProcessIconPart15.png', (0, 0)),
        ('ProcessIconPart16.png', (0, 0)),
        ('ProcessIconPart17.png', (0, 0)),
        ('ProcessIconPart18.png', (0, 0)),
        ('ProcessIconPart19.png', (0, 0)),
        ('ProcessIconPart20.png', (0, 0)),
        ('ProcessIconPart21.png', (0, 0)),
        ('ProcessIconPart22.png', (0, 0)),
        ('ProcessIconPart23.png', (0, 0)),
        ('ProcessIconPart24.png', (0, 0)),
        ('ErrorOpenImage1.png', (0, 0)),
        ('ErrorOpenImage2.png', (0, 0)),
        ('ChooseContourModeTips.png', (0, 0)),
        ('ImageUploadedIcon.png', (0, 0)),
        ('StatisticUploadedIcon.png', (0, 0)),
        ('FirstContourModeButton.png', (0, 0)),
        ('SecondContourModeButton.png', (0, 0)),
        ('ThirdContourModeButton.png', (0, 0)),
        ('StartCreatingButtonRealesed.png', (0, 0)),
        ('SettingsButtonRealesed.png', (0, 0)),
        ('SettingsButtonConfigureContourImage.png', (0, 0)),
        ('StartCreatingButtonClamped.png', (0, 0)),
        ('StartCreatingButtonConfigureContourImage.png', (0, 0)),
        ('SettingsButtonClamped.png', (0, 0)),
        ('HomeButtonRealesed.png', (0, 0)),
        ('HomeButtonClamped.png', (0, 0)),
        ('InfoContourModeButtonRealesed.png', (0, 0)),
        ('InfoContourModeButtonClamped.png', (0, 0)),
        ('BackButtonRealesed.png', (0, 0)),
        ('BackButtonClamped.png', (0, 0)),
        ('ChooseOrDropButtonRealesed.png', (0, 0)),
        ('ChooseButtonClamped.png', (0, 0)),
        ('DropButtonClamped.png', (0, 0)),
        ('ConfirmButtonRealesed.png', (0, 0)),
        ('ConfirmButtonClamped.png', (0, 0)),
        ('ChooseAnotherImageButtonRealesed.png', (0, 0)),
        ('ChooseAnotherImageButtonClamped.png', (0, 0)),
        ('DownloadButtonRealesed.png', (0, 0)),
        ('DownloadButtonClamped.png', (0, 0)),
        ('CancelButtonRealesed.png', (0, 0)),
        ('CancelButtonClamped.png', (0, 0)),
        ('SaveButtonRealesed.png', (0, 0)),
        ('SaveButtonClamped.png', (0, 0)),
        ('RenameButtonContourImageRealesed.png', (0, 0)),
        ('RenameButtonContourImageClamped.png', (0, 0)),
        ('DeleteButtonContourImageRealesed.png', (0, 0)),
        ('DeleteButtonContourImageClamped.png', (0, 0)),
        ('ConfigureContourImageBackground.png', (0, 0)),
        ('AcceptButtonRealesed.png', (0, 0)),
        ('AcceptButtonClamped.png', (0, 0)),
        ('CancelRenameButtonRealesed.png', (0, 0)),
        ('CancelRenameButtonClamped.png', (0, 0))
    ]



    PillowImagesUkrainian = {ImageInformation[0].replace('.png', ''): GetPillowImageUkrainian(ImageInformation[0], ImageInformation[1]) for ImageInformation in ImagesInformationUkrainian}

    TkImagesUkrainian = {PillowImage[0]: ImageTk.PhotoImage(PillowImage[1]) for PillowImage in PillowImagesUkrainian.items()}

    WidgetsInformationUkrainian = [
        ('BackgroundDetail1', TkImagesUkrainian['BackgroundDetail1'], 'fff9e9'),
        ('BackgroundDetail2', TkImagesUkrainian['BackgroundDetail2'], 'fff9e9'),
        ('BackgroundDetail3', TkImagesUkrainian['BackgroundDetail3'], 'fff9e9'),
        ('BackgroundDetail4', TkImagesUkrainian['BackgroundDetail4'], 'fff9e9'),
        ('BackgroundDetail5', TkImagesUkrainian['BackgroundDetail5'], 'fff9e9'),
        ('IBNGTextIcon', TkImagesUkrainian['IBNGTextIcon'], 'fff9e9'),
        ('ProcessFilePlace1', TkImagesUkrainian['ProcessFilePlace'], 'fff9e9'),
        ('ProcessFilePlace2', TkImagesUkrainian['ProcessFilePlace'], 'fff9e9'),
        ('ProcessFilePlace3', TkImagesUkrainian['ProcessFilePlace'], 'fff9e9'),
        ('ProcessFilePlace4', TkImagesUkrainian['ProcessFilePlace'], 'fff9e9'),
        ('YourContentText', TkImagesUkrainian['YourContentText'], 'fff7d9'),
        ('AllCreationsHereText', TkImagesUkrainian['AllCreationsHereText'], 'fff9e9'),
        ('ModeFirstTip', TkImagesUkrainian['ModeFirstTip'], 'fff9e9'),
        ('ModeSecondTip', TkImagesUkrainian['ModeSecondTip'], 'fff9e9'),
        ('ModeThirdTip', TkImagesUkrainian['ModeThirdTip'], 'fff9e9'),
        ('SettingsText', TkImagesUkrainian['SettingsText'], 'fff7d9'),
        ('LanguageText', TkImagesUkrainian['LanguageText'], 'fff7d9'),
        ('ExportSettingsPlaceButton', TkImagesUkrainian['ExportSettingsPlaceButtonRealesed'], 'fff9e9'),
        ('LanguageSettingsPlaceButton', TkImagesUkrainian['LanguageSettingsPlaceButtonRealesed'], 'fff9e9'),
        ('PriorityLanguageSettingsPlaceButton', TkImagesUkrainian['PriorityLanguageSettingsPlaceButtonRealesed'], 'fff9e9'),
        ('ColorSetsSettingsPlaceButton', TkImagesUkrainian['ColorSetsSettingsPlaceButtonRealesed'], 'fff9e9'),
        ('ChooseContourModeText', TkImagesUkrainian['ChooseContourModeText'], 'fff7d9'),
        ('InstractionText', TkImagesUkrainian['InstractionText'], 'fff7d9'),
        ('SelectAnImageText', TkImagesUkrainian['SelectAnImageText'], 'fff7d9'),
        ('SelectAContourText', TkImagesUkrainian['SelectAContourText'], 'fff7d9'),
        ('ImageProcessingText', TkImagesUkrainian['ImageProcessingText'], 'fff9e9'),
        ('PromptText', TkImagesUkrainian['PromptText'], 'fff9e9'),
        ('ProcessText', TkImagesUkrainian['ProcessText'], 'fff7d9'),
        ('ColorSetsText', TkImagesUkrainian['ColorSetsText'], 'fff7d9'),
        ('ExpectedColorsText', TkImagesUkrainian['ExpectedColorsText'], 'fff9e9'),
        ('RealColorsText', TkImagesUkrainian['RealColorsText'], 'fff9e9'),
        ('ImageStatisticsCreatedText', TkImagesUkrainian['ImageStatisticsCreatedText'], 'fff9e9'),
        ('PaletteCreatedText', TkImagesUkrainian['PaletteCreatedText'], 'fff9e9'),
        ('StockImageColorCreatedText', TkImagesUkrainian['StockImageColorCreatedText'], 'fff9e9'),
        ('ImageByNumberCreatedText', TkImagesUkrainian['ImageByNumberCreatedText'], 'fff9e9'),
        ('ImageStatisticsResultFileText', TkImagesUkrainian['ImageStatisticsResultFileText'], 'fff9e9'),
        ('PaletteResultFileText', TkImagesUkrainian['PaletteResultFileText'], 'fff9e9'),
        ('StockImageColorResultFileText', TkImagesUkrainian['StockImageColorResultFileText'], 'fff9e9'),
        ('ImageByNumberResultFileText', TkImagesUkrainian['ImageByNumberResultFileText'], 'fff9e9'),
        ('SelectColorsFromStockText', TkImagesUkrainian['SelectColorsFromStockText'], 'fff7d9'),
        ('ChooseColorsFromStockText', TkImagesUkrainian['ChooseColorsFromStockText'], 'fff7d9'),
        ('ChooseColorsFromStockText', TkImagesUkrainian['ChooseColorsFromStockText'], 'fff7d9'),
        ('ThisPageIsNotAvailableYet', TkImagesUkrainian['ThisPageIsNotAvailableYet'], 'fff9e9'),
        ('TextFileIcon', TkImagesUkrainian['TextFileIcon'], 'fbf1ca'),
        ('PaletteCreateIcon', TkImagesUkrainian['PaletteCreateIcon'], 'fbf1ca'),
        ('ImageByNumberIcon', TkImagesUkrainian['ImageByNumberIcon'], 'fbf1ca'),
        ('ImageByColorFromStockIcon', TkImagesUkrainian['ImageByColorFromStockIcon'], 'fbf1ca'),
        ('TextFileResultFileIcon', TkImagesUkrainian['TextFileResultFileIcon'], 'fff9e9'),
        ('PaletteResultFileIcon', TkImagesUkrainian['PaletteResultFileIcon'], 'fff9e9'),
        ('ImageByNumberResultFileIcon', TkImagesUkrainian['ImageByNumberResultFileIcon'], 'fff9e9'),
        ('ImageByColorFromStockResultFileIcon', TkImagesUkrainian['ImageByColorFromStockResultFileIcon'], 'fff9e9'),
        ('ErrorOpenImage1', TkImagesUkrainian['ErrorOpenImage1'], 'fff9e9'),
        ('ErrorOpenImage2', TkImagesUkrainian['ErrorOpenImage2'], 'fff9e9'),
        ('ChooseContourModeTips', TkImagesUkrainian['ChooseContourModeTips'], 'fff9e9'),
        ('FirstContourModeButton', TkImagesUkrainian['FirstContourModeButton'], 'fff9e9'),
        ('SecondContourModeButton', TkImagesUkrainian['SecondContourModeButton'], 'fff9e9'),
        ('ThirdContourModeButton', TkImagesUkrainian['ThirdContourModeButton'], 'fff9e9'),
        ('StartCreatingButton', TkImagesUkrainian['StartCreatingButtonRealesed'], 'fff9e9'),
        ('ImageUploadedIcon', TkImagesUkrainian['ImageUploadedIcon'], 'fff7d9'),
        ('StatisticUploadedIcon', TkImagesUkrainian['StatisticUploadedIcon'], 'fff7d9'),
        ('SettingsButton', TkImagesUkrainian['SettingsButtonRealesed'], 'fff9e9'),
        ('AcceptButton', TkImagesUkrainian['AcceptButtonRealesed'], 'fff9e9'),
        ('CancelRenameButton', TkImagesUkrainian['CancelRenameButtonRealesed'], 'fff9e9'),
        ('HomeButton', TkImagesUkrainian['HomeButtonRealesed'], 'fff7d9'),
        ('DownloadButton', TkImagesUkrainian['DownloadButtonRealesed'], 'fff7d9'),
        ('BackButton', TkImagesUkrainian['BackButtonRealesed'], 'fff7d9'),
        ('ChooseOrDropButton', TkImagesUkrainian['ChooseOrDropButtonRealesed'], 'fff9e9'),
        ('ConfirmButton', TkImagesUkrainian['ConfirmButtonRealesed'], 'fff9e9'),
        ('ChooseAnotherImageButton', TkImagesUkrainian['ChooseAnotherImageButtonRealesed'], 'fff9e9'),
        ('ProcessIcon', TkImagesUkrainian['ProcessIconPart6'], 'fff9e9'),
        ('SaveButton', TkImagesUkrainian['SaveButtonRealesed'], 'fff9e9'),
        ('CancelButton', TkImagesUkrainian['CancelButtonRealesed'], 'fff7d9'),
        ('RenameButtonContourImage', TkImagesUkrainian['RenameButtonContourImageRealesed'], 'fff7d9'),
        ('DeleteButtonContourImage', TkImagesUkrainian['DeleteButtonContourImageRealesed'], 'fff7d9')
    ]


    WidgetsUkrainian = {WidgetInformation[0]: Label(IBNGWindow, image=WidgetInformation[1], bg="#"+WidgetInformation[2], bd=0) for WidgetInformation in WidgetsInformationUkrainian}





    if SystemLanguage=="English":
        PillowImages=PillowImagesEnglish
        TkImages=TkImagesEnglish
        WidgetsInformation=WidgetsInformationEnglish
        Widgets=WidgetsEnglish
    elif SystemLanguage=="Ukrainian":
        PillowImages=PillowImagesUkrainian
        TkImages=TkImagesUkrainian
        WidgetsInformation=WidgetsInformationUkrainian
        Widgets=WidgetsUkrainian
        
















    PillowButtonContourImages = []
    TkButtonContourImages = []
    PillowButtonContourImageSettingsClamped = []
    TkButtonContourImageSettingsClamped = []
    PillowButtonContourImageConfigureContourImage = []
    TkButtonContourImageConfigureContourImage = []
    CreatedImages=[ResultImage for ResultImage in os.listdir(ApplicationPath+'/Cash/ResultsFiles') if os.path.isdir(os.path.join(ApplicationPath+'/Cash/ResultsFiles', ResultImage))]
    CreatedImages = sorted(CreatedImages, key=lambda File: os.stat(ApplicationPath+'/Cash/ResultsFiles/'+File).st_birthtime, reverse=True)
    for CreatedImageNumber, CreatedImage in enumerate(CreatedImages):
        if len(os.listdir(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage))<5:
            if os.path.exists(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage):
                shutil.rmtree(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage)
        else:
            CreatedImageSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12).getbbox(CreatedImage)
            CreatedImageSize=CreatedImageSize[2]-CreatedImageSize[0]
            if CreatedImageSize<133:
                CreatedImageText=CreatedImage
            else:
                CreatedImageText=CreatedImage
                while CreatedImageSize>=133:
                    CreatedImageSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12).getbbox(CreatedImageText+'...')
                    CreatedImageSize=CreatedImageSize[2]-CreatedImageSize[0]
                    CreatedImageText=CreatedImageText[:-1]
                CreatedImageText+='...'
            PillowButtonContourImages.append(Image.open(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage+'/ButtonContourImage.png'))
            PillowButtonContourImagesDraw=ImageDraw.Draw(PillowButtonContourImages[-1])
            PillowButtonContourImagesDraw.text((9, 176), CreatedImageText, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12), fill=(255, 176, 0, 255))
            TkButtonContourImages.append(ImageTk.PhotoImage(PillowButtonContourImages[-1]))
            PillowButtonContourImageSettingsClamped.append(Image.open(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage+'/ButtonContourImageSettingsClamped.png'))
            PillowButtonContourImageSettingsClampedDraw=ImageDraw.Draw(PillowButtonContourImageSettingsClamped[-1])
            PillowButtonContourImageSettingsClampedDraw.text((9, 176), CreatedImageText, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12), fill=(255, 176, 0, 255))
            TkButtonContourImageSettingsClamped.append(ImageTk.PhotoImage(PillowButtonContourImageSettingsClamped[-1]))
            PillowButtonContourImageConfigureContourImage.append(Image.open(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage+'/ButtonContourImageConfigureContourImage.png'))
            PillowButtonContourImageConfigureContourImageDraw=ImageDraw.Draw(PillowButtonContourImageConfigureContourImage[-1])
            PillowButtonContourImageConfigureContourImageDraw.text((9, 176), CreatedImageText, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12), fill=(255, 176, 0, 255))
            TkButtonContourImageConfigureContourImage.append(ImageTk.PhotoImage(PillowButtonContourImageConfigureContourImage[-1]))

      


    IBNGWindow.after(100, OpenProgramAnimation, 0)





IBNGWindow.lift()
IBNGWindow.focus_force()
IBNGWindow.wm_title("Image By Number Genearator")
IBNGWindowWidth=int(IBNGWindow.winfo_screenwidth()//1.5)
IBNGWindowHeight=int(IBNGWindow.winfo_screenheight()//1.5)
IBNGWindowX=int((IBNGWindow.winfo_screenwidth() - IBNGWindowWidth) // 2)
IBNGWindowY=int((IBNGWindow.winfo_screenheight() - IBNGWindowHeight) // 2)
IBNGWindow.geometry(str(IBNGWindowWidth)+'x'+str(IBNGWindowHeight)+'+'+str(IBNGWindowX)+'+'+str(IBNGWindowY))
IBNGWindow['bg']="#fff9e9"













def OpenStartWindow():
    global IBNGIconPillowImage
    global IBNGIconImage
    global IBNGIcon
    global IBNGTextIconPillowImage
    global IBNGTextIconImage
    global IBNGTextIcon
    IBNGIconPillowImage=Image.open(GetDataFilePath('English/ImageByNumberGeneratorIcon.png')).resize((150, 150))
    IBNGIconImage = ImageTk.PhotoImage(IBNGIconPillowImage)
    IBNGIcon = Label(IBNGWindow, image=IBNGIconImage, bg="#fff9e9")
    IBNGIcon.place(relx=0.5, y=300, anchor='center')

    IBNGTextIconPillowImage=Image.open(GetDataFilePath('English/IBNGTextIcon.png')).resize((150, 49))
    IBNGTextIconImage = ImageTk.PhotoImage(IBNGTextIconPillowImage)
    IBNGTextIcon = Label(IBNGWindow, image=IBNGTextIconImage, bg="#fff9e9")
    IBNGTextIcon.place(relx=0.5, y=425, anchor='center')
    IBNGWindow.update()
    UploadResources()
    IBNGWindow.minsize(700, 650)




def OpenProgramAnimation(Alpha):
    global IBNGTextIconImage
    global IBNGIconImage
    if Alpha>-254:
        Alpha-= 1
        IBNGIconImage = ImageTk.PhotoImage(IBNGIconPillowImage.point(lambda Transparent:Transparent+Alpha))
        IBNGIcon['image']=IBNGIconImage
        IBNGTextIconImage = ImageTk.PhotoImage(IBNGTextIconPillowImage.point(lambda Transparent:Transparent+Alpha))
        IBNGTextIcon['image']=IBNGTextIconImage
        IBNGWindow.after(1, OpenProgramAnimation, Alpha)
    else:
        [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
        [IBNGWindow.unbind_all(Event) for Event in Bindings]
        [IBNGWindow.unbind(Event) for Event in Bindings]
        for WindowElement in IBNGWindow.winfo_children():
           WindowElement.destroy()
        OpenMainWindow()





def OpenMainWindow():
   global IsEnterSettingsButton
   global IsEnterStartCreatingButton
   global ScrollCanvas
   global ScrollFrame
   global Widgets
   global ContourImageNumberButtons
   global SettingsIsClicked
   
   [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
   [IBNGWindow.unbind_all(Event) for Event in Bindings]
   [IBNGWindow.unbind(Event) for Event in Bindings]

   
   for WindowElement in IBNGWindow.winfo_children():
       WindowElement.destroy()
   WidgetsInWindow=['IBNGTextIcon', 'AcceptButton', 'CancelRenameButton', 'BackgroundDetail1', 'BackgroundDetail2', 'BackgroundDetail4', 'BackgroundDetail5', 'YourContentText', 'AllCreationsHereText', 'StartCreatingButton', 'SettingsButton', 'RenameButtonContourImage', 'DeleteButtonContourImage']
   Widgets = {WidgetInformation[0]: Label(IBNGWindow, image=WidgetInformation[1], bg="#"+WidgetInformation[2], bd=0) for WidgetInformation in WidgetsInformation if WidgetInformation[0] in WidgetsInWindow}

   IBNGWindow.update()

   
   Widgets['IBNGTextIcon'].place(y=45, relx=0.5, anchor='center')

   Widgets['BackgroundDetail1'].place(y=131, relx=0.5, anchor='center')
   
   Widgets['BackgroundDetail2'].place(relx=0.5, rely=1, anchor='s')

   Widgets['YourContentText'].place(y=131, relx=0.5, anchor='center')

   ScrollCanvas=Canvas(IBNGWindow, height=610, width=500, bg="#fff9e9", bd=0, highlightbackground="#fff9e9")
   

   CreatedImages=[ResultImage for ResultImage in os.listdir(ApplicationPath+'/Cash/ResultsFiles') if os.path.isdir(os.path.join(ApplicationPath+'/Cash/ResultsFiles', ResultImage))]


   if len(CreatedImages)==0:
      Widgets['AllCreationsHereText'].place(y=11, relx=0.5, rely=0.5, anchor='center')
   else:
      ScrollCanvas.place(y=170, relx=0.5, rely=0, anchor='n')

      ScrollFrame=Frame(ScrollCanvas, height=150*len(CreatedImages)-50 if len(CreatedImages) % 2 == 0 else 150*(len(CreatedImages)+1)-50, width=500, bg="#fff9e9")

      
      ScrollCanvas.create_window((0,0), window=ScrollFrame, anchor="nw")

      ContourImageNumberButtons=[]

      for TkButtonContourImageNumber, TkButtonContourImage in enumerate(TkButtonContourImages):
         if TkButtonContourImageNumber % 2 == 0:
            ContourImageNumberButtons.append(Label(ScrollFrame, image=TkButtonContourImage, bg="#fff9e9", bd=0))
            ContourImageNumberButtons[-1].place(x=-150, y=150*TkButtonContourImageNumber+20, relx=0.5, rely=0, anchor='n')
            ContourImageNumberButtons[-1].bind('<Button-1>', ContourImageNumberButtonsOnClick)
            ContourImageNumberButtons[-1].bind('<ButtonRelease-1>', ContourImageNumberButtonsRealese)
         else:
            ContourImageNumberButtons.append(Label(ScrollFrame, image=TkButtonContourImage, bg="#fff9e9", bd=0))
            ContourImageNumberButtons[-1].place(x=150, y=150*(TkButtonContourImageNumber-1)+20, relx=0.5, rely=0, anchor='n')
            ContourImageNumberButtons[-1].bind('<Button-1>', ContourImageNumberButtonsOnClick)
            ContourImageNumberButtons[-1].bind('<ButtonRelease-1>', ContourImageNumberButtonsRealese)

      ScrollCanvas.bind('<Configure>', lambda Event:ScrollCanvas.configure(scrollregion=(0, 0, 1000, 150*len(CreatedImages)-50 if len(CreatedImages) % 2 == 0 else 150*(len(CreatedImages)+1)-50 ) if 150*len(CreatedImages)-50>IBNGWindow.winfo_height()-290 or 150*(len(CreatedImages)+1)-50>IBNGWindow.winfo_height()-290 else (0,0,500,IBNGWindow.winfo_height()-290)))

      def IncreaseTimer():
          global ScrollbarHideTimer
          global ScrollbarHide
          ScrollbarHideTimer+=1
          if ScrollbarHideTimer>50000 and ScrollbarHide==True:
              if Scrollbar.winfo_exists():
                  Scrollbar.place_forget()
          else:
              IBNGWindow.after(1, IncreaseTimer)

      def MouseScrollbar(Event):
          global ScrollbarHideTimer
          global ScrollbarHide
          if Event.keysym=='Down' or Event.keysym=='Up':
              Force=-(1/(len(CreatedImages)*30)) if Event.keysym=='Up' else (1/(len(CreatedImages)*30))
              ScrollCanvas.yview_moveto(ScrollCanvas.yview()[0]+Force if ScrollCanvas.yview()[0]+Force > 0 else 0)
          else:
              Force=-(1/(len(CreatedImages)*50)*Event.delta)
              ScrollCanvas.yview_moveto(ScrollCanvas.yview()[0]+Force if ScrollCanvas.yview()[0]+Force > 0 else 0)

          

          if Scrollbar.place_info()=={}:
              Scrollbar.place( x=0, y=28, relx=1, rely=0.5, anchor='e', height=int(IBNGWindow.winfo_height()-278) )
          ScrollbarHideTimer=0
          ScrollbarHide=True
          IBNGWindow.after(1, IncreaseTimer)

      ScrollCanvas.bind_all('<MouseWheel>', MouseScrollbar)
      IBNGWindow.bind("<Up>", MouseScrollbar)
      IBNGWindow.bind("<Down>", MouseScrollbar)
      

      Scrollbar=ttk.Scrollbar(IBNGWindow, orient='vertical', command=ScrollCanvas.yview)


      ScrollbarStyle = ThemedStyle(Scrollbar)

      ScrollbarStyle.set_theme("arc")

      def FocusInScrollbar(Event):
          global ScrollbarHideTimer
          global ScrollbarHide
          ScrollbarHideTimer=0
          ScrollbarHide=False



      def FocusOutScrollbar(Event):
          global ScrollbarHideTimer
          global ScrollbarHide
          ScrollbarHideTimer=0
          ScrollbarHide=True




      Scrollbar.bind('<Button-1>', FocusInScrollbar)

      Scrollbar.bind('<ButtonRelease-1>', FocusOutScrollbar)


      ScrollCanvas.configure(yscrollcommand=Scrollbar.set)


   Widgets['StartCreatingButton'].place(y=-58, relx=0.5, rely=1, anchor='s')
   IsEnterStartCreatingButton=False

   Widgets['StartCreatingButton'].bind('<Enter>', StartCreatingButtonOnEnter)
   Widgets['StartCreatingButton'].bind('<Leave>', StartCreatingButtonOnLeave)
   Widgets['StartCreatingButton'].bind("<Button-1>", StartCreatingButtonOnClick)
   Widgets['StartCreatingButton'].bind("<ButtonRelease-1>", StartCreatingButtonRelease)

   Widgets['SettingsButton']['bg']='#fff9e9'
   Widgets['SettingsButton'].place(x=-27, y=16, relx=1, rely=0, anchor='ne')
   IsEnterSettingsButton=False

   Widgets['SettingsButton'].bind('<Enter>', SettingsButtonOnEnter)
   Widgets['SettingsButton'].bind('<Leave>', SettingsButtonOnLeave)
   Widgets['SettingsButton'].bind("<Button-1>", SettingsButtonOnClick)
   Widgets['SettingsButton'].bind("<ButtonRelease-1>", SettingsButtonRelease)


   



   SettingsIsClicked=False



   Widgets['StartCreatingButton'].lift()

   IBNGWindow.minsize(700, 650)
   

   
   def OnWindowResize(Event):
      if len(CreatedImages) != 0:
         ScrollCanvas.configure( height=int(IBNGWindow.winfo_height()-290) )
         if Scrollbar.place_info()!={}:
            Scrollbar.place( x=0, y=28, relx=1, rely=0.5, anchor='e', height=int(IBNGWindow.winfo_height()-278) )
      
         
   IBNGWindow.bind("<Configure>", OnWindowResize)





#Start Creating Button Animation

def StartCreatingButtonOnClick(Event):
    TkImages['StartCreatingButtonClamped'] = ImageTk.PhotoImage(PillowImages['StartCreatingButtonClamped'])
    Widgets['StartCreatingButton']['image'] = TkImages['StartCreatingButtonClamped']


def StartCreatingButtonRelease(Event):
    TkImages['StartCreatingButtonRealesed'] = ImageTk.PhotoImage(PillowImages['StartCreatingButtonRealesed'])
    Widgets['StartCreatingButton']['image'] = TkImages['StartCreatingButtonRealesed']
    if IsEnterStartCreatingButton == True:
        def GoToAnotherPage():
            [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
            [IBNGWindow.unbind_all(Event) for Event in Bindings]
            [IBNGWindow.unbind(Event) for Event in Bindings]
            for WindowElement in IBNGWindow.winfo_children():
                WindowElement.destroy()
            OpenSelectImageWindow()
        IBNGWindow.after(100, GoToAnotherPage)
   


def StartCreatingButtonOnEnter(Event):
   global IsEnterStartCreatingButton
   IsEnterStartCreatingButton=True

def StartCreatingButtonOnLeave(Event):
   global IsEnterStartCreatingButton
   IsEnterStartCreatingButton=False



#Home Button Animation

def HomeButtonOnClick(Event):
    TkImages['HomeButtonClamped'] = ImageTk.PhotoImage(PillowImages['HomeButtonClamped'])
    Widgets['HomeButton']['image'] = TkImages['HomeButtonClamped']


def HomeButtonRelease(Event):
    TkImages['HomeButtonRealesed'] = ImageTk.PhotoImage(PillowImages['HomeButtonRealesed'])
    Widgets['HomeButton']['image'] = TkImages['HomeButtonRealesed']
    if IsEnterHomeButton == True:
        def GoToAnotherPage():
            [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
            [IBNGWindow.unbind_all(Event) for Event in Bindings]
            [IBNGWindow.unbind(Event) for Event in Bindings]
            for WindowElement in IBNGWindow.winfo_children():
                WindowElement.destroy()
            OpenMainWindow()
        IBNGWindow.after(100, GoToAnotherPage)
   


def HomeButtonOnEnter(Event):
   global IsEnterHomeButton
   IsEnterHomeButton=True

def HomeButtonOnLeave(Event):
   global IsEnterHomeButton
   IsEnterHomeButton=False







def OpenSelectImageWindow():
    global IsEnterBackButton
    global IsEnterChooseButton
    global Widgets
    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
    [IBNGWindow.unbind_all(Event) for Event in Bindings]
    [IBNGWindow.unbind(Event) for Event in Bindings]
    for WindowElement in IBNGWindow.winfo_children():
       WindowElement.destroy()
    WidgetsInWindow=['BackgroundDetail3', 'SelectAnImageText', 'ChooseOrDropButton', 'BackButton', 'ErrorOpenImage1', 'ErrorOpenImage2', 'ConfirmButton', 'ChooseAnotherImageButton']
    Widgets = {WidgetInformation[0]: Label(IBNGWindow, image=WidgetInformation[1], bg="#"+WidgetInformation[2], bd=0) for WidgetInformation in WidgetsInformation if WidgetInformation[0] in WidgetsInWindow}

    

    Widgets['BackgroundDetail3'].place(rely=0, relx=0.5, anchor='n')


    Widgets['SelectAnImageText'].place(y=25, rely=0, relx=0.5, anchor='n')



    Widgets['ChooseOrDropButton'].place(relx=0.5, rely=0.5, anchor='center')

    IsEnterChooseButton=False


    Widgets['ChooseOrDropButton'].drop_target_register(DND_FILES)
    Widgets['ChooseOrDropButton'].dnd_bind('<<DropEnter>>', DropButtonEnter)
    Widgets['ChooseOrDropButton'].dnd_bind('<<DropLeave>>', DropButtonLeave)
    Widgets['ChooseOrDropButton'].dnd_bind('<<Drop>>', DropButtonRelease)
    Widgets['ChooseOrDropButton'].bind('<Enter>', ChooseButtonOnEnter)
    Widgets['ChooseOrDropButton'].bind('<Leave>', ChooseButtonOnLeave)
    Widgets['ChooseOrDropButton'].bind("<Button-1>", ChooseButtonOnClick)
    Widgets['ChooseOrDropButton'].bind("<ButtonRelease-1>", ChooseButtonRelease)



    Widgets['BackButton'].place(x=60, y=24, relx=0, rely=0, anchor='nw')

    IsEnterBackButton=False
    Widgets['BackButton'].bind('<Enter>', BackButtonOnEnter)
    Widgets['BackButton'].bind('<Leave>', BackButtonOnLeave)
    Widgets['BackButton'].bind("<Button-1>", BackButtonOnClick)
    Widgets['BackButton'].bind("<ButtonRelease-1>", lambda Event:BackButtonRelease(Event, OpenMainWindow))



#Back Button Animation

def BackButtonOnClick(Event):
    TkImages['BackButtonClamped'] = ImageTk.PhotoImage(PillowImages['BackButtonClamped'])
    Widgets['BackButton']['image'] = TkImages['BackButtonClamped']


def BackButtonRelease(Event, BackWindow, StopThreading=None):
    global StopThreadBool
    TkImages['BackButtonRealesed'] = ImageTk.PhotoImage(PillowImages['BackButtonRealesed'])
    Widgets['BackButton']['image'] = TkImages['BackButtonRealesed']
    if IsEnterBackButton == True:
        def GoToAnotherPage(BackWindow, StopThreading=None):
            global StopThreadBool
            if StopThreading!=None:
                StopThreadingId = next((Thread for _, Thread in threading._active.items() if Thread is StopThreading), None).ident
                ctypes.pythonapi.PyThreadState_SetAsyncExc(StopThreadingId, ctypes.py_object(SystemExit))
                StopThreadBool=True
               
            Widgets['BackButton']['bg']='#fff7d9'
            [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
            [IBNGWindow.unbind_all(Event) for Event in Bindings]
            [IBNGWindow.unbind(Event) for Event in Bindings]
            for WindowElement in IBNGWindow.winfo_children():
                WindowElement.destroy()
            BackWindow()
        IBNGWindow.after(100, lambda:GoToAnotherPage(BackWindow, StopThreading=StopThreading))
   


def BackButtonOnEnter(Event):
   global IsEnterBackButton
   IsEnterBackButton=True

def BackButtonOnLeave(Event):
   global IsEnterBackButton
   IsEnterBackButton=False



#Choose Or Drop Button







def DropButtonEnter(Event):
   def DropButtonEnterAnimate(Width, Height):
      if Width > 492:
         Width -= 2
         Height -= 1
         TkImages['DropButtonClamped'] = ImageTk.PhotoImage(PillowImages['DropButtonClamped'].resize((Width, Height)))
         Widgets['ChooseOrDropButton']['image'] = TkImages['DropButtonClamped']
         IBNGWindow.after(1, DropButtonEnterAnimate, Width, Height)

   Widgets['ErrorOpenImage1'].place_forget()
   Widgets['ErrorOpenImage2'].place_forget()
   DropButtonEnterAnimate(500, 250)




def DropButtonLeave(Event):
   def DropButtonEnterAnimate(Width, Height):
      if Width < 500:
         Width += 2
         Height += 1
         TkImages['ChooseOrDropButtonRealesed'] = ImageTk.PhotoImage(PillowImages['ChooseOrDropButtonRealesed'].resize((Width, Height)))
         Widgets['ChooseOrDropButton']['image'] = TkImages['ChooseOrDropButtonRealesed']
         IBNGWindow.after(1, DropButtonEnterAnimate, Width, Height)
   DropButtonEnterAnimate(492, 246)

def DropButtonRelease(Event):
   def DropButtonEnterAnimate(Width, Height):
      global IsEnterConfirmButton
      global SelectedImagePath
      if Width < 500:
         Width += 2
         Height += 1
         TkImages['ChooseOrDropButtonRealesed'] = ImageTk.PhotoImage(PillowImages['ChooseOrDropButtonRealesed'].resize((Width, Height)))
         Widgets['ChooseOrDropButton']['image'] = TkImages['ChooseOrDropButtonRealesed']
         IBNGWindow.after(1, DropButtonEnterAnimate, Width, Height)
      else:
         SelectedImages=[]
      
         SelectedImagePath=Event.data.replace('{', '').replace('}', '')
         SelectedImages=int(SelectedImagePath.count('.png'))+int(SelectedImagePath.count('.jpg'))+int(SelectedImagePath.count('.jpeg'))
         if SelectedImages==1:
            if '.png' in Event.data or '.jpg' in Event.data or '.jpeg' in Event.data:
                Widgets['ChooseOrDropButton'].place_forget()

                SelectedImage=Image.open(SelectedImagePath).convert("RGBA")
                WidthSelectedImage, HeightSelectedImage=SelectedImage.size
                if WidthSelectedImage/850 >= HeightSelectedImage/369:
                    SelectedImageResize=SelectedImage.resize((850, int(850/WidthSelectedImage*HeightSelectedImage)))
                else:
                    SelectedImageResize=SelectedImage.resize((int(369/HeightSelectedImage*WidthSelectedImage), 369))

                SelectedImage = SelectedImage.quantize(colors=16).convert('RGBA')
                ImageArray = np.array(SelectedImage)
                ImageArray[..., 3][ImageArray[..., 3] > 250] = 255
                SelectedImage = Image.fromarray(ImageArray)

                PillowImages['SelectedImage']=SelectedImage
                WidthSelectedImage, HeightSelectedImage=SelectedImage.size
                TkImages['SelectedImage']=ImageTk.PhotoImage(SelectedImageResize)
                Widgets['SelectedImage']=Label(IBNGWindow, image=TkImages['SelectedImage'], bg="#fff9e9", bd=0)
                Widgets['SelectedImage'].place(x=0, y=-38, rely=0.5, relx=0.5, anchor='center')



                Widgets['ConfirmButton'].place(x=0, y=-105, relx=0.5, rely=1, anchor='s')

                IsEnterConfirmButton=False

                Widgets['ConfirmButton'].bind('<Enter>', ConfirmButtonOnEnter)
                Widgets['ConfirmButton'].bind('<Leave>', ConfirmButtonOnLeave)
                Widgets['ConfirmButton'].bind("<Button-1>", ConfirmButtonOnClick)
                Widgets['ConfirmButton'].bind("<ButtonRelease-1>", lambda Event: ConfirmButtonRelease(Event))


               
                Widgets['ChooseAnotherImageButton'].place(x=0, y=-40, relx=0.5, rely=1, anchor='s')


                IsEnterChooseAnotherImageButton=False

                Widgets['ChooseAnotherImageButton'].bind('<Enter>', ChooseAnotherImageButtonOnEnter)
                Widgets['ChooseAnotherImageButton'].bind('<Leave>', ChooseAnotherImageButtonOnLeave)
                Widgets['ChooseAnotherImageButton'].bind("<Button-1>", ChooseAnotherImageButtonOnClick)
                Widgets['ChooseAnotherImageButton'].bind("<ButtonRelease-1>", lambda Event:ChooseAnotherImageButtonRelease(Event))
            else:
               Widgets['ErrorOpenImage2'].place(y=-50, relx=0.5, rely=1, anchor='s')
         else:
            Widgets['ErrorOpenImage1'].place(y=-50, relx=0.5, rely=1, anchor='s')
            
            
   DropButtonEnterAnimate(492, 246)
   


def ChooseButtonOnClick(Event):
   def ChooseButtonEnterAnimate(Width, Height):
      if Width > 492:
         Width -= 2
         Height -= 1
         TkImages['ChooseButtonClamped'] = ImageTk.PhotoImage(PillowImages['ChooseButtonClamped'].resize((Width, Height)))
         Widgets['ChooseOrDropButton']['image'] = TkImages['ChooseButtonClamped']
         IBNGWindow.after(1, ChooseButtonEnterAnimate, Width, Height)

   Widgets['ErrorOpenImage1'].place_forget()
   Widgets['ErrorOpenImage2'].place_forget()
   ChooseButtonEnterAnimate(500, 250)




def ChooseButtonRelease(Event):
   global IsEnterConfirmButton
   global IsEnterChooseAnotherImageButton
   global SelectedImagePath
   
   def ChooseButtonEnterAnimate(Width, Height):
      if Width < 500:
         Width += 2
         Height += 1
         TkImages['ChooseOrDropButtonRealesed'] = ImageTk.PhotoImage(PillowImages['ChooseOrDropButtonRealesed'].resize((Width, Height)))
         Widgets['ChooseOrDropButton']['image'] = TkImages['ChooseOrDropButtonRealesed']
         IBNGWindow.after(1, ChooseButtonEnterAnimate, Width, Height)
      
   if IsEnterChooseButton == True:
      SelectedImagePath=filedialog.askopenfilename(title='Choose an image', filetypes=[("Image Files", "*.png *.jpg *.jpeg"), ("All Files", "*.*")])
      ChooseButtonEnterAnimate(492, 246)
      if SelectedImagePath!='':
         if '.png' in SelectedImagePath or '.jpg' in SelectedImagePath or '.jpeg' in SelectedImagePath:
            Widgets['ChooseOrDropButton'].place_forget()

            SelectedImage=Image.open(SelectedImagePath).convert("RGBA")
            WidthSelectedImage, HeightSelectedImage=SelectedImage.size
            if WidthSelectedImage/850 >= HeightSelectedImage/369:
                SelectedImageResize=SelectedImage.resize((850, int(850/WidthSelectedImage*HeightSelectedImage)))
            else:
                SelectedImageResize=SelectedImage.resize((int(369/HeightSelectedImage*WidthSelectedImage), 369))
            SelectedImage = SelectedImage.quantize(colors=16).convert('RGBA')
            ImageArray = np.array(SelectedImage)
            ImageArray[..., 3][ImageArray[..., 3] > 250] = 255
            SelectedImage = Image.fromarray(ImageArray).copy()
            
            PillowImages['SelectedImage']=SelectedImage
            TkImages['SelectedImage']=ImageTk.PhotoImage(SelectedImageResize)
            Widgets['SelectedImage']=Label(IBNGWindow, image=TkImages['SelectedImage'], bg="#fff9e9", bd=0)
            Widgets['SelectedImage'].place(x=0, y=-38, rely=0.5, relx=0.5, anchor='center')



            Widgets['ConfirmButton'].place(x=0, y=-105, relx=0.5, rely=1, anchor='s')
            

            IsEnterConfirmButton=False

            Widgets['ConfirmButton'].bind('<Enter>', ConfirmButtonOnEnter)
            Widgets['ConfirmButton'].bind('<Leave>', ConfirmButtonOnLeave)
            Widgets['ConfirmButton'].bind("<Button-1>", ConfirmButtonOnClick)
            Widgets['ConfirmButton'].bind("<ButtonRelease-1>", lambda Event: ConfirmButtonRelease(Event))


            
            Widgets['ChooseAnotherImageButton'].place(x=0, y=-40, relx=0.5, rely=1, anchor='s')


            IsEnterChooseAnotherImageButton=False

            Widgets['ChooseAnotherImageButton'].bind('<Enter>', ChooseAnotherImageButtonOnEnter)
            Widgets['ChooseAnotherImageButton'].bind('<Leave>', ChooseAnotherImageButtonOnLeave)
            Widgets['ChooseAnotherImageButton'].bind("<Button-1>", ChooseAnotherImageButtonOnClick)
            Widgets['ChooseAnotherImageButton'].bind("<ButtonRelease-1>", lambda Event:ChooseAnotherImageButtonRelease(Event))
         else:
            Widgets['ErrorOpenImage2'].place(y=-50, relx=0.5, rely=1, anchor='s')

   else:
      ChooseButtonEnterAnimate(492, 246)
            
   


def ChooseButtonOnEnter(Event):
   global IsEnterChooseButton
   IsEnterChooseButton=True

def ChooseButtonOnLeave(Event):
   global IsEnterChooseButton
   IsEnterChooseButton=False




#Choose Another Image Button Animation

def ChooseAnotherImageButtonOnClick(Event):
    TkImages['ChooseAnotherImageButtonClamped'] = ImageTk.PhotoImage(PillowImages['ChooseAnotherImageButtonClamped'])
    Widgets['ChooseAnotherImageButton']['image'] = TkImages['ChooseAnotherImageButtonClamped']


def ChooseAnotherImageButtonRelease(Event):
    TkImages['ChooseAnotherImageButtonRealesed'] = ImageTk.PhotoImage(PillowImages['ChooseAnotherImageButtonRealesed'])
    Widgets['ChooseAnotherImageButton']['image'] = TkImages['ChooseAnotherImageButtonRealesed']
    if IsEnterChooseAnotherImageButton == True:
        def GoToAnotherPage():
            for WindowElement in IBNGWindow.winfo_children():
                WindowElement.destroy()
            OpenSelectImageWindow()
        IBNGWindow.after(100, GoToAnotherPage)
       


def ChooseAnotherImageButtonOnEnter(Event):
   global IsEnterChooseAnotherImageButton
   IsEnterChooseAnotherImageButton=True

def ChooseAnotherImageButtonOnLeave(Event):
   global IsEnterChooseAnotherImageButton
   IsEnterChooseAnotherImageButton=False


#Confirm Button Animation

def ConfirmButtonOnClick(Event):
    TkImages['ConfirmButtonClamped'] = ImageTk.PhotoImage(PillowImages['ConfirmButtonClamped'])
    Widgets['ConfirmButton']['image'] = TkImages['ConfirmButtonClamped']


def ConfirmButtonRelease(Event):
    TkImages['ConfirmButtonRealesed'] = ImageTk.PhotoImage(PillowImages['ConfirmButtonRealesed'])
    Widgets['ConfirmButton']['image'] = TkImages['ConfirmButtonRealesed']
    if IsEnterConfirmButton == True:
        def GoToAnotherPage():
            for WindowElement in IBNGWindow.winfo_children():
                WindowElement.destroy()

            IBNGWindow.after(0, OpenProcessingUploadedImageWindow)
        IBNGWindow.after(100, GoToAnotherPage)
   


def ConfirmButtonOnEnter(Event):
   global IsEnterConfirmButton
   IsEnterConfirmButton=True

def ConfirmButtonOnLeave(Event):
   global IsEnterConfirmButton
   IsEnterConfirmButton=False







def OpenProcessingUploadedImageWindow():
    global IsEnterBackButton
    global ColorsPercentInImage
    global ColorsInRGB
    global GetColorsInImageAndCreatePaletteColorsThreading
    global EndColors
    global GetColorsInImageAndCreatePaletteColorsIsEnd
    global StopThreading
    global StopThreadBool
    global Widgets
    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
    [IBNGWindow.unbind_all(Event) for Event in Bindings]
    [IBNGWindow.unbind(Event) for Event in Bindings]
    for WindowElement in IBNGWindow.winfo_children():
       WindowElement.destroy()
    WidgetsInWindow=['ProcessIcon', 'ImageProcessingText', 'BackButton']
    Widgets = {WidgetInformation[0]: Label(IBNGWindow, image=WidgetInformation[1], bg="#"+WidgetInformation[2], bd=0) for WidgetInformation in WidgetsInformation if WidgetInformation[0] in WidgetsInWindow}



    StopThreadBool=False


    Widgets['ProcessIcon'].place(x=0, y=-57, relx=0.5, rely=0.5, anchor='center')


    Widgets['ImageProcessingText'].place(x=0, y=103, relx=0.5, rely=0.5, anchor='center')




    ColorsPercentInImage=[]
    ColorsInRGB=[]
    EndColors=[]
    GetColorsInImageAndCreatePaletteColorsIsEnd=False






    Widgets['BackButton']['bg']='#fff9e9'
    Widgets['BackButton'].place(x=60, y=24, relx=0, rely=0, anchor='nw')

    IsEnterBackButton=False

    Widgets['BackButton'].bind('<Enter>', BackButtonOnEnter)
    Widgets['BackButton'].bind('<Leave>', BackButtonOnLeave)
    Widgets['BackButton'].bind("<Button-1>", BackButtonOnClick)
    Widgets['BackButton'].bind("<ButtonRelease-1>", lambda Event:BackButtonRelease(Event, OpenSelectImageWindow, GetColorsInImageAndCreatePaletteColorsThreading))


    ProcessIconAnimation(1)
    
    GetColorsInImageAndCreatePaletteColorsThreading=threading.Thread(target=GetColorsInImageAndCreatePaletteColors)
    GetColorsInImageAndCreatePaletteColorsThreading.start()



   
    def OnWindowResize(Event):
        if 'ProcessIcon' in Widgets:
            Widgets['ProcessIcon'].update_idletasks()


    IBNGWindow.bind("<Configure>", OnWindowResize)



   


def ProcessIconAnimation(AnimationIcon):
   if GetColorsInImageAndCreatePaletteColorsIsEnd==True:
      [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
      [IBNGWindow.unbind_all(Event) for Event in Bindings]
      [IBNGWindow.unbind(Event) for Event in Bindings]
      for WindowElement in IBNGWindow.winfo_children():
          WindowElement.destroy()
      IBNGWindow.resizable(True, True)
      OpenSelectColorsFromStockWindow()
   elif StopThreadBool == True:
      pass
   else:
      if 'ProcessIcon' in Widgets:
          Widgets['ProcessIcon']['image']=TkImages['ProcessIconPart'+str(AnimationIcon)]
      if AnimationIcon==4:
         AnimationIcon+=1
         IBNGWindow.after(100, ProcessIconAnimation, AnimationIcon)
      elif AnimationIcon==8:
         AnimationIcon+=1
         IBNGWindow.after(100, ProcessIconAnimation, AnimationIcon)
      elif AnimationIcon==12:
         AnimationIcon+=1
         IBNGWindow.after(150, ProcessIconAnimation, AnimationIcon)
      elif AnimationIcon==16:
         AnimationIcon+=1
         IBNGWindow.after(100, ProcessIconAnimation, AnimationIcon)
      elif AnimationIcon==20:
         AnimationIcon+=1
         IBNGWindow.after(100, ProcessIconAnimation, AnimationIcon)
      elif AnimationIcon==24:
         AnimationIcon=1
         IBNGWindow.after(150, ProcessIconAnimation, AnimationIcon)
      else:
         AnimationIcon+=1
         IBNGWindow.after(50, ProcessIconAnimation, AnimationIcon)



      
def FindSimilarColor(TargetColor):
   global EndColors
   ColorsAndDistance=[]
   for ColorStock in ColorsStock:
     ColorsAndDistance.append([ColorStock, math.sqrt((TargetColor[0] - ColorStock[0]) ** 2 + (TargetColor[1] - ColorStock[1]) ** 2 + (TargetColor[2] - ColorStock[2]) ** 2)])

   ColorsAndDistance=sorted(ColorsAndDistance, key=lambda Distance: Distance[1])
   SameSimilar=0
   while True:
     if SameSimilar == len(ColorsAndDistance)-1 or ColorsAndDistance[SameSimilar][0] not in EndColors:
         EndColors.append(ColorsAndDistance[SameSimilar][0])
         return ColorsAndDistance[SameSimilar][0]
     else:
         SameSimilar+=1
            


def GetColorsInImageAndCreatePaletteColors():
    global ColorsInRGB
    global ColorsPercentInImage
    global GetColorsInImageAndCreatePaletteColorsIsEnd
    global EndColors
    global PillowImages



    try:
        AllColorsInfo=[Color for Color in PillowImages['SelectedImage'].getcolors() if Color[0]> PillowImages['SelectedImage'].size[0] * PillowImages['SelectedImage'].size[1]*0.00086 and Color[1][3]==255]

        ColorsInRGB=sorted([Color[1] for Color in AllColorsInfo])

        PixelCount=sum([Color[0] for Color in AllColorsInfo])

        ColorsPercentInImage=[]

        for Count, Color in AllColorsInfo:
            ColorPercent = (100 / PixelCount) * Count
            ColorPercent = round(round(ColorPercent * 10, 1) / 10, 1)
            ColorsPercentInImage.append(ColorPercent)
       

        RealColorImages=Image.new('RGBA', (len(ColorsInRGB)*95-15, 70), color = (255, 255, 255,0))

        for ColorInRGB in ColorsInRGB:
            NumberOfColor=ColorsInRGB.index(ColorInRGB)
            ColorImage=Image.new('RGBA', (710, 710), color = (255, 255, 255,0))
            ColorImageDraw=ImageDraw.Draw(ColorImage)
            ColorImageDraw.rectangle([(30, 30), (675, 675)], fill=ColorInRGB)
            ColorImage.paste(Image.open(GetDataFilePath('English/PaletteColor.png')), (0, 0), mask=Image.open(GetDataFilePath('English/PaletteColor.png')))
            if len(str(NumberOfColor+1))==1:
                ColorImageDraw.text((90, 35), str(NumberOfColor+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))
            else:
                ColorImageDraw.text((30, 35), str(NumberOfColor+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))
            
            RealColorImage=ColorImage.resize((70, 70))
            RealColorImages.paste(RealColorImage, (NumberOfColor*95+5, 0), mask=RealColorImage)

        TkImages['RealColorImages']=ImageTk.PhotoImage(RealColorImages)



        for ColorInRGB in ColorsInRGB:
            NumberOfColor=ColorsInRGB.index(ColorInRGB)
            Color=FindSimilarColor(ColorInRGB)
            ColorImage=Image.new('RGBA', (710, 710), color = (255, 255, 255,0))
            ColorImageDraw=ImageDraw.Draw(ColorImage)
            ColorImageDraw.rectangle([(30, 30), (675, 675)], fill=Color)
            ColorImage.paste(Image.open(GetDataFilePath('English/PaletteRealStockColor.png')), (0, 0), mask=Image.open(GetDataFilePath('English/PaletteRealStockColor.png')))
            if len(str(NumberOfColor+1))==1:
                ColorImageDraw.text((90, 35), str(NumberOfColor+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))
            else:
                ColorImageDraw.text((30, 35), str(NumberOfColor+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))


            if len(str(ColorsStock.index(Color)+1))==1:
                ColorImageDraw.text((574, 544), str(ColorsStock.index(Color)+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 100), fill=(255, 173, 0, 255))
            else:
                ColorImageDraw.text((543, 544), str(ColorsStock.index(Color)+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 100), fill=(255, 173, 0, 255))

            
            PillowImages['RealStockColorImages'+str(NumberOfColor+1)]=ColorImage.resize((70, 70))
            TkImages['RealStockColorImages'+str(NumberOfColor+1)]=ImageTk.PhotoImage(ColorImage.resize((70, 70)))
            
            
            ColorClampedImage=Image.new('RGBA', (710, 710), color = (255, 255, 255,0))
            ColorClampedImageDraw=ImageDraw.Draw(ColorClampedImage)
            ColorClampedImageDraw.rectangle([(30, 30), (675, 675)], fill=Color)
            ColorClampedImage.paste(Image.open(GetDataFilePath('English/PaletteRealStockColorClamped.png')), (0, 0), mask=Image.open(GetDataFilePath('English/PaletteRealStockColorClamped.png')))
            if len(str(NumberOfColor+1))==1:
                ColorClampedImageDraw.text((90, 35), str(NumberOfColor+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))
            else:
                ColorClampedImageDraw.text((30, 35), str(NumberOfColor+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))


            if len(str(ColorsStock.index(Color)+1))==1:
                ColorClampedImageDraw.text((574, 544), str(ColorsStock.index(Color)+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 100), fill=(255, 173, 0, 255))
            else:
                ColorClampedImageDraw.text((543, 544), str(ColorsStock.index(Color)+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 100), fill=(255, 173, 0, 255))

            PillowImages['RealStockColorImagesClamped'+str(NumberOfColor+1)]=ColorClampedImage.resize((70, 70))
            TkImages['RealStockColorImagesClamped'+str(NumberOfColor+1)]=ImageTk.PhotoImage(ColorClampedImage.resize((70, 70)))

            
        for ColorStock in ColorsStock:
            NumberOfColor=ColorsStock.index(ColorStock)
            ColorImage=Image.new('RGBA', (710, 710), color = (255, 255, 255,0))
            ColorImageDraw=ImageDraw.Draw(ColorImage)
            ColorImageDraw.rectangle([(30, 30), (675, 675)], fill=ColorStock)
            ColorImage.paste(Image.open(GetDataFilePath('English/PaletteColor.png')), (0, 0), mask=Image.open(GetDataFilePath('English/PaletteColor.png')))
            if len(str(NumberOfColor+1))==1:
                ColorImageDraw.text((90, 35), str(NumberOfColor+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))
            else:
                ColorImageDraw.text((30, 35), str(NumberOfColor+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))


            PillowImages['StockColorImages'+str(NumberOfColor+1)]=ColorImage.resize((70, 70))
            TkImages['StockColorImages'+str(NumberOfColor+1)]=ImageTk.PhotoImage(ColorImage.resize((70, 70)))

            ColorClampedImage=Image.new('RGBA', (710, 710), color = (255, 255, 255,0))
            ColorClampedImageDraw=ImageDraw.Draw(ColorClampedImage)
            ColorClampedImageDraw.rectangle([(30, 30), (675, 675)], fill=ColorStock)
            ColorClampedImage.paste(Image.open(GetDataFilePath('English/PaletteColorClamped.png')), (0, 0), mask=Image.open(GetDataFilePath('English/PaletteColorClamped.png')))
            if len(str(NumberOfColor+1))==1:
                ColorClampedImageDraw.text((90, 35), str(NumberOfColor+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))
            else:
                ColorClampedImageDraw.text((30, 35), str(NumberOfColor+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))

            PillowImages['StockColorImagesClamped'+str(NumberOfColor+1)]=ColorClampedImage.resize((70, 70))
            TkImages['StockColorImagesClamped'+str(NumberOfColor+1)]=ImageTk.PhotoImage(ColorClampedImage.resize((70, 70)))
            
        for ColorStock in ColorsStock:
            NumberOfColor=ColorsStock.index(ColorStock)
            ColorImage=Image.new('RGBA', (710, 710), color = (255, 255, 255,0))
            ColorImageDraw=ImageDraw.Draw(ColorImage)
            ColorImageDraw.rectangle([(30, 30), (675, 675)], fill=ColorStock)
            ColorImage.paste(Image.open(GetDataFilePath('English/PaletteColor.png')), (0, 0), mask=Image.open(GetDataFilePath('English/PaletteColor.png')))
            if len(str(NumberOfColor+1))==1:
                ColorImageDraw.text((90, 35), str(NumberOfColor+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))
            else:
                ColorImageDraw.text((30, 35), str(NumberOfColor+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))

            ColorImage.paste(Image.open(GetDataFilePath('English/CrossedPaleteColor.png')), (0, 0), mask=Image.open(GetDataFilePath('English/CrossedPaleteColor.png')))
            PillowImages['CrossStockColorImages'+str(NumberOfColor+1)]=ColorImage.resize((70, 70))
            TkImages['CrossStockColorImages'+str(NumberOfColor+1)]=ImageTk.PhotoImage(ColorImage.resize((70, 70)))
            
            ColorClampedImage=Image.new('RGBA', (710, 710), color = (255, 255, 255,0))
            ColorClampedImageDraw=ImageDraw.Draw(ColorClampedImage)
            ColorClampedImageDraw.rectangle([(30, 30), (675, 675)], fill=ColorStock)
            ColorClampedImage.paste(Image.open(GetDataFilePath('English/PaletteColorClamped.png')), (0, 0), mask=Image.open(GetDataFilePath('English/PaletteColorClamped.png')))
            if len(str(NumberOfColor+1))==1:
                ColorClampedImageDraw.text((90, 35), str(NumberOfColor+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))
            else:
                ColorClampedImageDraw.text((30, 35), str(NumberOfColor+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))

            ColorClampedImage.paste(Image.open(GetDataFilePath('English/CrossedPaleteColorClamped.png')), (0, 0), mask=Image.open(GetDataFilePath('English/CrossedPaleteColorClamped.png')))
            PillowImages['CrossStockColorImagesClamped'+str(NumberOfColor+1)]=ColorClampedImage.resize((70, 70))
            TkImages['CrossStockColorImagesClamped'+str(NumberOfColor+1)]=ImageTk.PhotoImage(ColorClampedImage.resize((70, 70)))

            

        IBNGWindow.resizable(False, False)
        def EndFunction():
            global GetColorsInImageAndCreatePaletteColorsIsEnd
            GetColorsInImageAndCreatePaletteColorsIsEnd=True
        IBNGWindow.after(100, EndFunction)
    except Exception as Error:
        IBNGExcepthook()








def OpenSelectColorsFromStockWindow():
    global IsEnterHomeButton
    global RealStockImages
    global NumberOfColorClickedRealStockColor
    global IsEnterSaveButton
    global ScrollRealColorImagesCanvas
    global ScrollRealColorImagesFrame
    global ScrollRealStockColorImagesCanvas
    global ScrollRealStockColorImagesFrame
    global ScrollbarRealColorImages
    global ScrollbarRealStockColorImages
    global Widgets
    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
    [IBNGWindow.unbind_all(Event) for Event in Bindings]
    [IBNGWindow.unbind(Event) for Event in Bindings]
    for WindowElement in IBNGWindow.winfo_children():
       WindowElement.destroy()
    WidgetsInWindow=['BackgroundDetail3', 'SelectColorsFromStockText', 'RealColorsText', 'ExpectedColorsText', 'SaveButton', 'PromptText', 'HomeButton', 'CancelButton', 'ChooseColorsFromStockText']
    Widgets = {WidgetInformation[0]: Label(IBNGWindow, image=WidgetInformation[1], bg="#"+WidgetInformation[2], bd=0) for WidgetInformation in WidgetsInformation if WidgetInformation[0] in WidgetsInWindow}

    IBNGWindow.update()


    Widgets['BackgroundDetail3'].place(rely=0, relx=0.5, anchor='n')

    Widgets['SelectColorsFromStockText'].place(y=25, rely=0, relx=0.5, anchor='n')



    Widgets['RealColorsText'].place(y=147, rely=0, relx=0.5, anchor='n')


    
    ScrollRealColorImagesCanvas=Canvas(IBNGWindow, height=70, width=int(IBNGWindow.winfo_width()), bg="#fff9e9", bd=0, highlightbackground="#fff9e9")
    
    ScrollRealColorImagesCanvas.place(y=205, relx=0, rely=0, anchor='nw')

    ScrollRealColorImagesFrame=Frame(ScrollRealColorImagesCanvas, height=70, width=len(ColorsInRGB)*95+5, bg="#fff9e9")

    ScrollRealColorImagesCanvas.create_window((0,0), window=ScrollRealColorImagesFrame, anchor="nw")


    
    def MouseScrollbarRealColorImages(Event):
        if Event.keysym=='Right' or Event.keysym=='Left':
            Force=-(1/(len(ColorsInRGB)*10)) if Event.keysym=='Left' else (1/(len(ColorsInRGB)*10))
            ScrollRealColorImagesCanvas.xview_moveto(ScrollRealColorImagesCanvas.xview()[0]+Force if ScrollRealColorImagesCanvas.xview()[0]+Force > 0 else 0)
        else:
            Force=-(1/(len(ColorsInRGB)*50)*Event.delta)
            ScrollRealColorImagesCanvas.xview_moveto(ScrollRealColorImagesCanvas.xview()[0]+Force if ScrollRealColorImagesCanvas.xview()[0]+Force > 0 else 0)

          


    Widgets['RealColorImages']=Label(ScrollRealColorImagesFrame, image=TkImages['RealColorImages'], bg="#fff9e9", bd=0)
    Widgets['RealColorImages'].place(x=0, y=0)
    

    ScrollRealColorImagesCanvas.bind('<Configure>', lambda Event:ScrollRealColorImagesCanvas.configure(scrollregion=(0, 0, len(ColorsInRGB)*95+5, 70)))

    def ScrollRealColorImagesFrameOnEnter(Event):
        ScrollRealColorImagesFrame.bind_all('<Shift-MouseWheel>', MouseScrollbarRealColorImages)
        IBNGWindow.bind("<Left>", MouseScrollbarRealColorImages)
        IBNGWindow.bind("<Right>", MouseScrollbarRealColorImages)
        
    def ScrollRealColorImagesFrameOnLeave(Event):
        ScrollRealColorImagesFrame.unbind_all('<Shift-MouseWheel>')
        IBNGWindow.unbind("<Left>")
        IBNGWindow.unbind("<Right>")
    ScrollRealColorImagesFrame.bind('<Enter>', ScrollRealColorImagesFrameOnEnter)
    ScrollRealColorImagesFrame.bind('<Leave>', ScrollRealColorImagesFrameOnLeave)


    ScrollbarRealColorImages=ttk.Scrollbar(IBNGWindow, orient='horizontal', command=ScrollRealColorImagesCanvas.xview)


    if int(IBNGWindow.winfo_width()-10)<len(ColorsInRGB)*95+5:
        ScrollbarRealColorImages.place(x=5, y=285, relx=0, rely=0, anchor='nw', width=int(IBNGWindow.winfo_width()-10))

    ScrollbarRealColorImagesStyle = ThemedStyle(ScrollbarRealColorImages)

    ScrollbarRealColorImagesStyle.set_theme("arc")

    ScrollRealColorImagesCanvas.configure(xscrollcommand=ScrollbarRealColorImages.set)




    Widgets['ExpectedColorsText'].place(y=327, rely=0, relx=0.5, anchor='n')




    ScrollRealStockColorImagesCanvas=Canvas(IBNGWindow, height=70, width=int(IBNGWindow.winfo_width()), bg="#fff9e9", bd=0, highlightbackground="#fff9e9")
    
    ScrollRealStockColorImagesCanvas.place(y=385, relx=0, rely=0, anchor='nw')

    ScrollRealStockColorImagesFrame=Frame(ScrollRealStockColorImagesCanvas, height=70, width=len(ColorsInRGB)*95+5, bg="#fff9e9")

    ScrollRealStockColorImagesCanvas.create_window((0,0), window=ScrollRealStockColorImagesFrame, anchor="nw")


    
    def MouseScrollbarRealStockColorImages(Event):
        if Event.keysym=='Right' or Event.keysym=='Left':
            Force=-(1/(len(ColorsInRGB)*10)) if Event.keysym=='Left' else (1/(len(ColorsInRGB)*10))
            ScrollRealStockColorImagesCanvas.xview_moveto(ScrollRealStockColorImagesCanvas.xview()[0]+Force if ScrollRealStockColorImagesCanvas.xview()[0]+Force > 0 else 0)
        else:
            Force=-(1/(len(ColorsInRGB)*50)*Event.delta)
            ScrollRealStockColorImagesCanvas.xview_moveto(ScrollRealStockColorImagesCanvas.xview()[0]+Force if ScrollRealStockColorImagesCanvas.xview()[0]+Force > 0 else 0)
    

   
    RealStockImages={}
    for IndexColorInRGB, ColorInRGB in enumerate(ColorsInRGB):
        Widgets['RealStockColorImages'+str(IndexColorInRGB+1)]=Label(ScrollRealStockColorImagesFrame, image=TkImages['RealStockColorImages'+str(IndexColorInRGB+1)], bg="#fff9e9", bd=0)   
        Widgets['RealStockColorImages'+str(IndexColorInRGB+1)].place(x=IndexColorInRGB*95+5, y=0)
        Widgets['RealStockColorImages'+str(IndexColorInRGB+1)].bind('<Enter>', RealStockColorImageButtonOnEnter)
        Widgets['RealStockColorImages'+str(IndexColorInRGB+1)].bind('<Leave>', RealStockColorImageButtonOnLeave)
        Widgets['RealStockColorImages'+str(IndexColorInRGB+1)].bind("<Button-1>", RealStockColorImageButtonOnClick)
        Widgets['RealStockColorImages'+str(IndexColorInRGB+1)].bind("<ButtonRelease-1>", RealStockColorImageButtonRelease)
        RealStockImages[Widgets['RealStockColorImages'+str(IndexColorInRGB+1)]]='RealStockColorImages'+str(IndexColorInRGB+1)


    

    ScrollRealStockColorImagesCanvas.bind('<Configure>', lambda Event:ScrollRealStockColorImagesCanvas.configure(scrollregion=(0, 0, len(ColorsInRGB)*95+5, 70)))

    
    ScrollRealStockColorImagesFrame.bind('<Enter>', lambda Event:ScrollRealStockColorImagesFrame.bind_all('<Shift-MouseWheel>', MouseScrollbarRealStockColorImages))
    ScrollRealStockColorImagesFrame.bind('<Leave>', lambda Event:ScrollRealStockColorImagesFrame.unbind_all('<Shift-MouseWheel>'))
    def ScrollRealStockColorImagesFrameOnEnter(Event):
        ScrollRealStockColorImagesFrame.bind_all('<Shift-MouseWheel>', MouseScrollbarRealStockColorImages)
        IBNGWindow.bind("<Left>", MouseScrollbarRealStockColorImages)
        IBNGWindow.bind("<Right>", MouseScrollbarRealStockColorImages)
        
    def ScrollRealStockColorImagesFrameOnLeave(Event):
        ScrollRealStockColorImagesFrame.unbind_all('<Shift-MouseWheel>')
        IBNGWindow.unbind("<Left>")
        IBNGWindow.unbind("<Right>")
    ScrollRealStockColorImagesFrame.bind('<Enter>', ScrollRealStockColorImagesFrameOnEnter)
    ScrollRealStockColorImagesFrame.bind('<Leave>', ScrollRealStockColorImagesFrameOnLeave)


    ScrollbarRealStockColorImages=ttk.Scrollbar(IBNGWindow, orient='horizontal', command=ScrollRealStockColorImagesCanvas.xview)


    if int(IBNGWindow.winfo_width()-10)<len(ColorsInRGB)*95+5:
        ScrollbarRealStockColorImages.place(x=5, y=465, relx=0, rely=0, anchor='nw', width=int(IBNGWindow.winfo_width()-10))

    ScrollbarRealStockColorImagesStyle = ThemedStyle(ScrollbarRealStockColorImages)

    ScrollbarRealStockColorImagesStyle.set_theme("arc")

    ScrollRealStockColorImagesCanvas.configure(xscrollcommand=ScrollbarRealStockColorImages.set)
        

    NumberOfColorClickedRealStockColor=0



    Widgets['SaveButton'].place(y=500, rely=0, relx=0.5, anchor='n')

    IsEnterSaveButton=False

    Widgets['SaveButton'].bind('<Enter>', SaveButtonOnEnter)
    Widgets['SaveButton'].bind('<Leave>', SaveButtonOnLeave)
    Widgets['SaveButton'].bind("<Button-1>", SaveButtonOnClick)
    Widgets['SaveButton'].bind("<ButtonRelease-1>", SaveButtonRelease)

    Widgets['PromptText'].place(y=-45, rely=1, relx=0.5, anchor='s')




    Widgets['HomeButton'].place(x=-20, y=14, relx=1, rely=0, anchor='ne')
    
    if 'HomeButton' in Widgets and int(IBNGWindow.winfo_width())<1000:
        Widgets['HomeButton'].place(x=-1, y=14, relx=1, rely=0, anchor='ne')

    IsEnterHomeButton=False

    Widgets['HomeButton'].bind('<Enter>', HomeButtonOnEnter)
    Widgets['HomeButton'].bind('<Leave>', HomeButtonOnLeave)
    Widgets['HomeButton'].bind("<Button-1>", HomeButtonOnClick)
    Widgets['HomeButton'].bind("<ButtonRelease-1>", HomeButtonRelease)

    

 



    IBNGWindow.unbind("<Configure>")



    def OnWindowResize(Event):
        if 'HomeButton' in Widgets and int(IBNGWindow.winfo_width())<1000 and int(Widgets['HomeButton'].place_info()['x'])!=-1:
            Widgets['HomeButton'].place(x=-1, y=14, relx=1, rely=0, anchor='ne')
        elif 'HomeButton' in Widgets and int(IBNGWindow.winfo_width())>=1000 and int(Widgets['HomeButton'].place_info()['x'])!=-20:
            Widgets['HomeButton'].place(x=-20, y=14, relx=1, rely=0, anchor='ne')
            
        if len(ColorsInRGB) != 0 and ScrollRealColorImagesCanvas.winfo_exists()==1:
            ScrollRealColorImagesCanvas.configure( width=int(IBNGWindow.winfo_width()) )
            ScrollRealStockColorImagesCanvas.configure( width=int(IBNGWindow.winfo_width()) )
            if int(IBNGWindow.winfo_width()-10)<len(ColorsInRGB)*95+5:
                ScrollbarRealColorImages.place(x=5, y=285, relx=0, rely=0, anchor='nw', width=int(IBNGWindow.winfo_width()-10))
                ScrollbarRealStockColorImages.place(x=5, y=465, relx=0, rely=0, anchor='nw', width=int(IBNGWindow.winfo_width()-10))
            else:
                if ScrollbarRealColorImages.place_info()!={}:
                    ScrollbarRealColorImages.place_forget()
                if ScrollbarRealStockColorImages.place_info()!={}:
                    ScrollbarRealStockColorImages.place_forget()
                
          
             
    IBNGWindow.bind("<Configure>", OnWindowResize)

    IBNGWindow.update()
    IBNGWindow.update_idletasks()

    
    IBNGWindow.minsize(860, 700)
    




#Save Button Animation

def SaveButtonOnClick(Event):
    TkImages['SaveButtonClamped'] = ImageTk.PhotoImage(PillowImages['SaveButtonClamped'])
    Widgets['SaveButton']['image'] = TkImages['SaveButtonClamped']


def SaveButtonRelease(Event):
    TkImages['SaveButtonRealesed'] = ImageTk.PhotoImage(PillowImages['SaveButtonRealesed'])
    Widgets['SaveButton']['image'] = TkImages['SaveButtonRealesed']
    if IsEnterSaveButton == True:
        def GoToAnotherPage():
            for WindowElement in IBNGWindow.winfo_children():
               WindowElement.destroy()
            OpenProcessCreationWindow()
        IBNGWindow.after(100, GoToAnotherPage)

   


def SaveButtonOnEnter(Event):
   global IsEnterSaveButton
   IsEnterSaveButton=True

def SaveButtonOnLeave(Event):
   global IsEnterSaveButton
   IsEnterSaveButton=False





#Cancel Button Animation

def CancelButtonOnClick(Event):
    TkImages['CancelButtonClamped'] = ImageTk.PhotoImage(PillowImages['CancelButtonClamped'])
    Widgets['CancelButton']['image'] = TkImages['CancelButtonClamped']


def CancelButtonRelease(Event):
    TkImages['CancelButtonRealesed'] = ImageTk.PhotoImage(PillowImages['CancelButtonRealesed'])
    Widgets['CancelButton']['image'] = TkImages['CancelButtonRealesed']
    if IsEnterCancelButton == True:
        def GoToAnotherPage():
            for WindowElement in IBNGWindow.winfo_children():
               WindowElement.destroy()
            OpenSelectColorsFromStockWindow()
        IBNGWindow.after(100, GoToAnotherPage)


def CancelButtonOnEnter(Event):
   global IsEnterCancelButton
   IsEnterCancelButton=True

def CancelButtonOnLeave(Event):
   global IsEnterCancelButton
   IsEnterCancelButton=False





#Stock Color Image Button Animation
def StockColorImageButtonOnClick(Event):
    ClampedImage=StockImages[Event.widget].replace('StockColorImages', 'StockColorImagesClamped')
    Widgets[StockImages[Event.widget]]['image'] = TkImages[ClampedImage]


def StockColorImageButtonRelease(Event):
    global StockColorImages
    global NumberOfColorClickedRealStockColor
    Widgets[StockImages[Event.widget]]['image'] = TkImages[StockImages[Event.widget]]
    if IsEnterStockColorImageButton == StockImages[Event.widget]+'True':
        NumberOfColor=NumberOfColorClickedRealStockColor
        Color=ColorsStock[int(str(StockImages[Event.widget]).replace('StockColorImages', '').replace('Cross', ''))-1]
        ColorImage=Image.new('RGBA', (710, 710), color = (255, 255, 255,0))
        ColorImageDraw=ImageDraw.Draw(ColorImage)
        ColorImageDraw.rectangle([(30, 30), (675, 675)], fill=Color)
        ColorImage.paste(Image.open(GetDataFilePath('English/PaletteRealStockColor.png')), (0, 0), mask=Image.open(GetDataFilePath('English/PaletteRealStockColor.png')))
        if len(str(NumberOfColor))==1:
           ColorImageDraw.text((90, 35), str(NumberOfColor), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))
        else:
           ColorImageDraw.text((30, 35), str(NumberOfColor), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))


        if len(str(ColorsStock.index(Color)+1))==1:
           ColorImageDraw.text((574, 544), str(ColorsStock.index(Color)+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 100), fill=(255, 173, 0, 255))
        else:
           ColorImageDraw.text((543, 544), str(ColorsStock.index(Color)+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 100), fill=(255, 173, 0, 255))


        PillowImages['RealStockColorImages'+str(NumberOfColor)]=ColorImage.resize((70, 70))
        TkImages['RealStockColorImages'+str(NumberOfColor)]=ImageTk.PhotoImage(ColorImage.resize((70, 70)))
        Widgets['RealStockColorImages'+str(NumberOfColor)]['image']=TkImages['RealStockColorImages'+str(NumberOfColor)]
         
         
        ColorClampedImage=Image.new('RGBA', (710, 710), color = (255, 255, 255,0))
        ColorClampedImageDraw=ImageDraw.Draw(ColorClampedImage)
        ColorClampedImageDraw.rectangle([(30, 30), (675, 675)], fill=Color)
        ColorClampedImage.paste(Image.open(GetDataFilePath('English/PaletteRealStockColorClamped.png')), (0, 0), mask=Image.open(GetDataFilePath('English/PaletteRealStockColorClamped.png')))
        if len(str(NumberOfColor))==1:
            ColorClampedImageDraw.text((90, 35), str(NumberOfColor), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))
        else:
            ColorClampedImageDraw.text((30, 35), str(NumberOfColor), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))


        if len(str(ColorsStock.index(Color)+1))==1:
            ColorClampedImageDraw.text((574, 544), str(ColorsStock.index(Color)+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 100), fill=(255, 173, 0, 255))
        else:
            ColorClampedImageDraw.text((543, 544), str(ColorsStock.index(Color)+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 100), fill=(255, 173, 0, 255))

        PillowImages['RealStockColorImagesClamped'+str(NumberOfColor)]=ColorClampedImage.resize((70, 70))
        TkImages['RealStockColorImagesClamped'+str(NumberOfColor)]=ImageTk.PhotoImage(ColorClampedImage.resize((70, 70)))
         
        EndColors[NumberOfColor-1]=Color
        NumberOfColorClickedRealStockColor=0
        for WindowElement in IBNGWindow.winfo_children():
            WindowElement.destroy()
        OpenSelectColorsFromStockWindow()
            
            

            
   


def StockColorImageButtonOnEnter(Event):
   global IsEnterStockColorImageButton
   IsEnterStockColorImageButton=StockImages[Event.widget]+'True'

   

def StockColorImageButtonOnLeave(Event):
   global IsEnterStockColorImageButton
   if IsEnterStockColorImageButton==StockImages[Event.widget]+'True':
      IsEnterStockColorImageButton=StockImages[Event.widget]+'False'
      






def RealStockColorImageButtonOnClick(Event):
    ClampedImage=RealStockImages[Event.widget].replace('RealStockColorImages', 'RealStockColorImagesClamped')
    Widgets[RealStockImages[Event.widget]]['image'] = TkImages[ClampedImage]


def RealStockColorImageButtonRelease(Event):
    global StockImages
    global NumberOfColorClickedRealStockColor
    global Widgets
    global TkImages
    global BackgroundDetail4
    global ScrollStockColorImagesCanvas
    global ScrollStockColorImagesFrame
    global ScrollbarStockColorImages
    global ColorStockByWidth
    Widgets[RealStockImages[Event.widget]]['image'] = TkImages[RealStockImages[Event.widget]]

    if NumberOfColorClickedRealStockColor != 0:
        Widgets['RealStockColorImages'+str(NumberOfColorClickedRealStockColor)].bind('<Enter>', RealStockColorImageButtonOnEnter)
        Widgets['RealStockColorImages'+str(NumberOfColorClickedRealStockColor)].bind('<Leave>', RealStockColorImageButtonOnLeave)
        Widgets['RealStockColorImages'+str(NumberOfColorClickedRealStockColor)].bind("<Button-1>", RealStockColorImageButtonOnClick)
        Widgets['RealStockColorImages'+str(NumberOfColorClickedRealStockColor)].bind("<ButtonRelease-1>", RealStockColorImageButtonRelease)
        Widgets['RealStockColorImages'+str(NumberOfColorClickedRealStockColor)]['image'] = TkImages['RealStockColorImages'+str(NumberOfColorClickedRealStockColor)]
        Widgets['ChooseColorsFromStockText'].place_forget()
        IBNGWindow.unbind("<Configure>")
        ScrollStockColorImagesCanvas.destroy()
        ScrollStockColorImagesFrame.destroy()
        ScrollbarStockColorImages.destroy()
        for IndexColorStock, ColorStock in enumerate(ColorsStock):
            if ColorStock in EndColors:
                Widgets['CrossStockColorImages'+str(IndexColorStock+1)].destroy()
            else:
                Widgets['StockColorImages'+str(IndexColorStock+1)].destroy()
            
    
    
    if IsEnterRealStockColorImageButton == RealStockImages[Event.widget]+'True':
        Event.widget.unbind('<Enter>')
        Event.widget.unbind('<Leave>')
        Event.widget.unbind("<Button-1>")
        Event.widget.unbind("<ButtonRelease-1>")
        Widgets['PromptText'].place_forget()
        Widgets['SaveButton'].place_forget()
        BackgroundDetail4=Frame(IBNGWindow, bg='#fff7d9', height=530, width=1800, bd=0)
        BackgroundDetail4.lower()
        BackgroundDetail4.place(x=0, y=470, relx=0.5, rely=0, anchor='n')
        Widgets['ChooseColorsFromStockText'].place(x=0, y=480, relx=0.5, rely=0, anchor='n')
        Widgets['ChooseColorsFromStockText'].update()
        NumberOfColorClickedRealStockColor=int(str(RealStockImages[Event.widget]).replace('RealStockColorImages', ''))

        
        ScrollStockColorImagesCanvas=Canvas(IBNGWindow, height=int(IBNGWindow.winfo_height())-630, width=IBNGWindow.winfo_width(), bg="#fff7d9", bd=0, highlightbackground="#fff7d9")

        ScrollStockColorImagesCanvas.place(y=528, relx=0, rely=0, anchor='nw')

        ColorStockByWidth=int((IBNGWindow.winfo_width()+3)/95)

        ScrollStockColorImagesFrame=Frame(ScrollStockColorImagesCanvas, height=70+((math.ceil(len(ColorsStock)/ColorStockByWidth)-1)*90), width=1800, bg="#fff7d9")

        ScrollStockColorImagesCanvas.create_window((0,0), window=ScrollStockColorImagesFrame, anchor="nw")



        def MouseScrollbarStockColorImages(Event):
            if Event.keysym=='Up' or Event.keysym=='Down':
                Force=-(1/(len(ColorsStock))) if Event.keysym=='Up' else (1/(len(ColorsInRGB)))
                ScrollStockColorImagesCanvas.yview_moveto(ScrollStockColorImagesCanvas.yview()[0]+Force if ScrollStockColorImagesCanvas.yview()[0]+Force > 0 else 0)
            else:
                Force=-(1/(len(ColorsStock)*10)*Event.delta)
                ScrollStockColorImagesCanvas.yview_moveto(ScrollStockColorImagesCanvas.yview()[0]+Force if ScrollStockColorImagesCanvas.yview()[0]+Force > 0 else 0)


        StockImages={}
        for IndexColorStock, ColorStock in enumerate(ColorsStock):
           ColorStockRow=math.ceil((IndexColorStock+1)/ColorStockByWidth)-1
           ColorStockColumn=IndexColorStock-(ColorStockRow*ColorStockByWidth)
           if ColorStock in EndColors:
              Widgets['CrossStockColorImages'+str(IndexColorStock+1)]=Label(ScrollStockColorImagesFrame, image=TkImages['CrossStockColorImages'+str(IndexColorStock+1)], bg="#fff7d9", bd=0)
              Widgets['CrossStockColorImages'+str(IndexColorStock+1)].place(x=ColorStockColumn*95+45, y=35+(ColorStockRow*90), anchor='center')
              Widgets['CrossStockColorImages'+str(IndexColorStock+1)].bind('<Enter>', StockColorImageButtonOnEnter)
              Widgets['CrossStockColorImages'+str(IndexColorStock+1)].bind('<Leave>', StockColorImageButtonOnLeave)
              Widgets['CrossStockColorImages'+str(IndexColorStock+1)].bind("<Button-1>", StockColorImageButtonOnClick)
              Widgets['CrossStockColorImages'+str(IndexColorStock+1)].bind("<ButtonRelease-1>", StockColorImageButtonRelease)
              StockImages[Widgets['CrossStockColorImages'+str(IndexColorStock+1)]]='CrossStockColorImages'+str(IndexColorStock+1)
           else:
              Widgets['StockColorImages'+str(IndexColorStock+1)]=Label(ScrollStockColorImagesFrame, image=TkImages['StockColorImages'+str(IndexColorStock+1)], bg="#fff7d9", bd=0)
              Widgets['StockColorImages'+str(IndexColorStock+1)].place(x=ColorStockColumn*95+45, y=35+(ColorStockRow*90), anchor='center')
              Widgets['StockColorImages'+str(IndexColorStock+1)].bind('<Enter>', StockColorImageButtonOnEnter)
              Widgets['StockColorImages'+str(IndexColorStock+1)].bind('<Leave>', StockColorImageButtonOnLeave)
              Widgets['StockColorImages'+str(IndexColorStock+1)].bind("<Button-1>", StockColorImageButtonOnClick)
              Widgets['StockColorImages'+str(IndexColorStock+1)].bind("<ButtonRelease-1>", StockColorImageButtonRelease)
              StockImages[Widgets['StockColorImages'+str(IndexColorStock+1)]]='StockColorImages'+str(IndexColorStock+1)
        
        ScrollStockColorImagesCanvas.bind('<Configure>', lambda Event:ScrollStockColorImagesCanvas.configure(scrollregion=(0, 0, 1800, 70+((math.ceil(len(ColorsStock)/ColorStockByWidth)-1)*90) )))


        def ScrollStockColorImagesFrameOnEnter(Event):
            ScrollStockColorImagesFrame.bind_all('<MouseWheel>', MouseScrollbarStockColorImages)
            IBNGWindow.bind("<Down>", MouseScrollbarStockColorImages)
            IBNGWindow.bind("<Up>", MouseScrollbarStockColorImages)
            
        def ScrollStockColorImagesFrameOnLeave(Event):
            ScrollStockColorImagesFrame.unbind_all('<MouseWheel>')
            IBNGWindow.unbind("<Down>")
            IBNGWindow.unbind("<Up>")
        ScrollStockColorImagesFrame.bind('<Enter>', ScrollStockColorImagesFrameOnEnter)
        ScrollStockColorImagesFrame.bind('<Leave>', ScrollStockColorImagesFrameOnLeave)


        ScrollbarStockColorImages=ttk.Scrollbar(IBNGWindow, orient='vertical', command=ScrollStockColorImagesCanvas.yview)

        if 70+((math.ceil(len(ColorsStock)/ColorStockByWidth)-1)*90)>int(IBNGWindow.winfo_height())-630:
            ScrollbarStockColorImages.place(x=0, y=529, relx=1, rely=0, anchor='ne', height=int(IBNGWindow.winfo_height())-625)

        ScrollbarStockColorImagesStyle = ThemedStyle(ScrollbarStockColorImages)

        ScrollbarStockColorImagesStyle.set_theme("arc2")

        ScrollStockColorImagesCanvas.configure(yscrollcommand=ScrollbarStockColorImages.set)

        ColorStockByWidth=0


              
        Widgets['CancelButton'].place(x=0, y=-15, relx=0.5, rely=1, anchor='s')
        Widgets['CancelButton'].bind('<Enter>', CancelButtonOnEnter)
        Widgets['CancelButton'].bind('<Leave>', CancelButtonOnLeave)
        Widgets['CancelButton'].bind("<Button-1>", CancelButtonOnClick)
        Widgets['CancelButton'].bind("<ButtonRelease-1>", CancelButtonRelease)
        Widgets['CancelButton'].lift()


        def OnWindowResize(Event):
            global ColorStockByWidth
            if 'HomeButtonmeButton' in Widgets and int(IBNGWindow.winfo_width())<1000 and int(Widgets['HomeButton'].place_info()['x'])!=-1:
               Widgets['HomeButton'].place(x=-1, y=14, relx=1, rely=0, anchor='ne')
            elif 'HomeButton' in Widgets and int(IBNGWindow.winfo_width())>=1000 and int(Widgets['HomeButton'].place_info()['x'])!=-20:
               Widgets['HomeButton'].place(x=-20, y=14, relx=1, rely=0, anchor='ne')
               
            if len(ColorsInRGB) != 0:
               ScrollRealColorImagesCanvas.configure( width=int(IBNGWindow.winfo_width()) )
               ScrollRealStockColorImagesCanvas.configure( width=int(IBNGWindow.winfo_width()) )
               if int(IBNGWindow.winfo_width()-10)<len(ColorsInRGB)*95+5:
                   ScrollbarRealColorImages.place(x=5, y=285, relx=0, rely=0, anchor='nw', width=int(IBNGWindow.winfo_width()-10))
                   ScrollbarRealStockColorImages.place(x=5, y=465, relx=0, rely=0, anchor='nw', width=int(IBNGWindow.winfo_width()-10))
               else:
                   if ScrollbarRealColorImages.place_info()!={}:
                       ScrollbarRealColorImages.place_forget()
                   if ScrollbarRealStockColorImages.place_info()!={}:
                       ScrollbarRealStockColorImages.place_forget()
                        
            ColorStockByWidthNow=int((IBNGWindow.winfo_width()+3)/95)
            if ColorStockByWidth!=ColorStockByWidthNow:
                ScrollStockColorImagesFrame['height']=70+((math.ceil(len(ColorsStock)/ColorStockByWidthNow)-1)*90)
                for IndexColorStock, ColorStock in enumerate(ColorsStock):
                   ColorStockRow=math.ceil((IndexColorStock+1)/ColorStockByWidthNow)-1
                   ColorStockColumn=IndexColorStock-(ColorStockRow*ColorStockByWidthNow)
                   if ColorStock in EndColors:
                        Widgets['CrossStockColorImages'+str(IndexColorStock+1)].place(x=ColorStockColumn*95+45, y=35+(ColorStockRow*90), anchor='center')
                   else:
                        Widgets['StockColorImages'+str(IndexColorStock+1)].place(x=ColorStockColumn*95+45, y=35+(ColorStockRow*90), anchor='center')
                ScrollStockColorImagesCanvas.bind('<Configure>', lambda Event:ScrollStockColorImagesCanvas.configure(scrollregion=(0, 0, 1800, 70+((math.ceil(len(ColorsStock)/ColorStockByWidthNow)-1)*90) )))
                ColororStockByWidth=ColorStockByWidthNow
                ScrollStockColorImagesCanvas.configure(height=int(IBNGWindow.winfo_height())-630, width=IBNGWindow.winfo_width())
                if int(ScrollStockColorImagesFrame['height'])>int(ScrollStockColorImagesCanvas['height']):
                    ScrollbarStockColorImages.place(x=0, y=529, relx=1, rely=0, anchor='ne', height=int(IBNGWindow.winfo_height())-625)
                else:
                    if ScrollbarStockColorImages.place_info()!={}:
                        ScrollbarStockColorImages.place_forget()
              
                 
        IBNGWindow.bind("<Configure>", OnWindowResize)
        


def RealStockColorImageButtonOnEnter(Event):
   global IsEnterRealStockColorImageButton
   IsEnterRealStockColorImageButton=RealStockImages[Event.widget]+'True'

def RealStockColorImageButtonOnLeave(Event):
   global IsEnterRealStockColorImageButton
   if IsEnterRealStockColorImageButton==RealStockImages[Event.widget]+'True':
      IsEnterRealStockColorImageButton=RealStockImages[Event.widget]+'False'







def OpenProcessCreationWindow():
    global IsEnterBackButton
    global ImageStatisticsCreated
    global PaletteCreated
    global ProcessThreading
    global StockImageColorCreated
    global ImageByNumberCreated
    global StopThreadBool
    global Widgets
    global ProccesIconPosition
    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
    [IBNGWindow.unbind_all(Event) for Event in Bindings]
    [IBNGWindow.unbind(Event) for Event in Bindings]
    for WindowElement in IBNGWindow.winfo_children():
       WindowElement.destroy()
    WidgetsInWindow=['BackgroundDetail3', 'ProcessText', 'TextFileIcon', 'ProcessFilePlace4', 'ImageByColorFromStockIcon', 'StockImageColorCreatedText', 'ProcessIcon', 'ProcessFilePlace1', 'BackButton', 'ImageStatisticsCreatedText', 'ProcessFilePlace2', 'PaletteCreateIcon', 'PaletteCreatedText', 'ProcessFilePlace3', 'ImageByNumberIcon', 'ImageByNumberCreatedText']
    Widgets = {WidgetInformation[0]: Label(IBNGWindow, image=WidgetInformation[1], bg="#"+WidgetInformation[2], bd=0) for WidgetInformation in WidgetsInformation if WidgetInformation[0] in WidgetsInWindow}

##    IBNGWindow.update()
    

    Widgets['BackgroundDetail3'].place(y=0, relx=0.5, anchor='n')

    Widgets['ProcessText'].place(y=25, relx=0.5, anchor='n')



    Widgets['ProcessIcon']['bg']='#fbf1ca'
    Widgets['ProcessIcon'].place(x=-400, y=-120, relx=0.5, rely=0.5, anchor='center')

    Widgets['ProcessFilePlace1'].place(x=-400, y=-120, relx=0.5, rely=0.5, anchor='center')
    if int(IBNGWindow.winfo_width())<1100:
        Widgets['ProcessIcon'].place(x=79, y=-120, relx=0, rely=0.5, anchor='w')
        Widgets['ProcessFilePlace1'].place(x=19, y=-120, relx=0, rely=0.5, anchor='w')


    ImageStatisticsCreated=False
    PaletteCreated=False
    StockImageColorCreated=False
    ImageByNumberCreated=False
    StopThreadBool=False
    ProccesIconPosition=0
    ProcessCreationIconAnimation(1, 1)
    ProcessThreading=threading.Thread(target=CreateImageStatistics)
    ProcessThreading.start()




    Widgets['BackButton'].place(x=60, y=23, anchor='ne')

    IsEnterBackButton=False

    Widgets['BackButton'].bind('<Enter>', BackButtonOnEnter)
    Widgets['BackButton'].bind('<Leave>', BackButtonOnLeave)
    Widgets['BackButton'].bind("<Button-1>", BackButtonOnClick)
    Widgets['BackButton'].bind("<ButtonRelease-1>", lambda Event:BackButtonRelease(Event, OpenSelectColorsFromStockWindow, ProcessThreading))



    IBNGWindow.unbind("<Configure>")



   
    def OnWindowResize(Event):
        if 'ProcessIcon' in Widgets:
            Widgets['ProcessIcon'].update_idletasks()
        if 'ImageByNumberCreatedText' in Widgets and Widgets['ImageByNumberCreatedText'].place_info() != {} and int(IBNGWindow.winfo_height())<724 and Widgets['ImageByNumberCreatedText'].place_info()['anchor']=='center':
            Widgets['ImageByNumberCreatedText'].place(x=0, y=-6, relx=0.5, rely=1, anchor='s')
        elif 'ImageByNumberCreatedText' in Widgets and Widgets['ImageByNumberCreatedText'].place_info() != {} and int(IBNGWindow.winfo_height())>=724 and Widgets['ImageByNumberCreatedText'].place_info()['anchor']=='s':
            Widgets['ImageByNumberCreatedText'].place(x=0, y=343, relx=0.5, rely=0.5, anchor='center')
        if int(IBNGWindow.winfo_width())<1100:
            if ProccesIconPosition==0 and 'ProcessIcon' in Widgets and Widgets['ProcessIcon'].place_info() != {} and Widgets['ProcessIcon'].place_info()['anchor']=='center':
                Widgets['ProcessIcon'].place(x=79, y=-120, relx=0, rely=0.5, anchor='w')
            if ProccesIconPosition==2 and 'ProcessIcon' in Widgets and Widgets['ProcessIcon'].place_info() != {} and Widgets['ProcessIcon'].place_info()['anchor']=='center':
                Widgets['ProcessIcon'].place(x=-79, y=-120, relx=1, rely=0.5, anchor='e')
            if 'ProcessFilePlace1' in Widgets and Widgets['ProcessFilePlace1'].place_info() != {} and Widgets['ProcessFilePlace1'].place_info()['anchor']=='center':
                Widgets['ProcessFilePlace1'].place(x=19, y=-120, relx=0, rely=0.5, anchor='w')
            if 'ProcessFilePlace3' in Widgets and Widgets['ProcessFilePlace3'].place_info() != {} and Widgets['ProcessFilePlace3'].place_info()['anchor']=='center':
                Widgets['ProcessFilePlace3'].place(x=-19, y=-120, relx=1, rely=0.5, anchor='e')
            if 'ImageStatisticsCreatedText' in Widgets and Widgets['ImageStatisticsCreatedText'].place_info() != {} and Widgets['ImageStatisticsCreatedText'].place_info()['anchor']=='center':
                Widgets['ImageStatisticsCreatedText'].place(x=18, y=33, relx=0, rely=0.5, anchor='w')
            if 'StockImageColorCreatedText' in Widgets and Widgets['StockImageColorCreatedText'].place_info() != {} and Widgets['StockImageColorCreatedText'].place_info()['anchor']=='center':
                Widgets['StockImageColorCreatedText'].place(x=-12, y=33, relx=1, rely=0.5, anchor='e')
            if 'TextFileIcon' in Widgets and Widgets['TextFileIcon'].place_info() != {} and Widgets['TextFileIcon'].place_info()['anchor']=='center':
                Widgets['TextFileIcon'].place(x=65, y=-120, relx=0, rely=0.5, anchor='w')
            if 'ImageByColorFromStockIcon' in Widgets and Widgets['ImageByColorFromStockIcon'].place_info() != {} and Widgets['ImageByColorFromStockIcon'].place_info()['anchor']=='center':
                Widgets['ImageByColorFromStockIcon'].place(x=-65, y=-120, relx=1, rely=0.5, anchor='e')
        else:
            if 'ProcessFilePlace1' in Widgets and Widgets['ProcessFilePlace1'].place_info() != {} and Widgets['ProcessFilePlace1'].place_info()['anchor']=='w':
                Widgets['ProcessFilePlace1'].place(x=-400, y=-120, relx=0.5, rely=0.5, anchor='center')
            if 'ProcessFilePlace3' in Widgets and Widgets['ProcessFilePlace3'].place_info() != {} and Widgets['ProcessFilePlace3'].place_info()['anchor']=='e':
                Widgets['ProcessFilePlace3'].place(x=400, y=-120, relx=0.5, rely=0.5, anchor='center')
            if 'ImageStatisticsCreatedText' in Widgets and Widgets['ImageStatisticsCreatedText'].place_info() != {} and Widgets['ImageStatisticsCreatedText'].place_info()['anchor']=='w':
                Widgets['ImageStatisticsCreatedText'].place(x=-400, y=33, relx=0.5, rely=0.5, anchor='center')
            if 'StockImageColorCreatedText' in Widgets and Widgets['StockImageColorCreatedText'].place_info() != {} and Widgets['StockImageColorCreatedText'].place_info()['anchor']=='e':
                Widgets['StockImageColorCreatedText'].place(x=400, y=33, relx=0.5, rely=0.5, anchor='center')
            if 'TextFileIcon' in Widgets and Widgets['TextFileIcon'].place_info() != {} and Widgets['TextFileIcon'].place_info()['anchor']=='w':
                Widgets['TextFileIcon'].place(x=-400, y=-120, relx=0.5, rely=0.5, anchor='center')
            if 'ImageByColorFromStockIcon' in Widgets and Widgets['ImageByColorFromStockIcon'].place_info() != {} and Widgets['ImageByColorFromStockIcon'].place_info()['anchor']=='e':
                Widgets['ImageByColorFromStockIcon'].place(x=400, y=-120, relx=0.5, rely=0.5, anchor='center')
            if ProccesIconPosition==0 and 'ProcessIcon' in Widgets and Widgets['ProcessIcon'].place_info() != {} and Widgets['ProcessIcon'].place_info()['anchor']=='w':
                Widgets['ProcessIcon'].place(x=-400, y=-120, relx=0.5, rely=0.5, anchor='center')
            if ProccesIconPosition==2 and 'ProcessIcon' in Widgets and Widgets['ProcessIcon'].place_info() != {} and Widgets['ProcessIcon'].place_info()['anchor']=='e':
                Widgets['ProcessIcon'].place(x=400, y=-120, relx=0.5, rely=0.5, anchor='center')


    IBNGWindow.bind("<Configure>", OnWindowResize)







def ProcessCreationIconAnimation(AnimationIcon, StepOfProcessCreation):
   global ProcessThreading
   global StopThreadBool
   global ProccesIconPosition
   if StopThreadBool == True:
      pass
   elif ImageStatisticsCreated==True and StepOfProcessCreation==1:
      StepOfProcessCreation+=1
      ProccesIconPosition+=1
      Widgets['ProcessIcon'].place_forget()
      IBNGWindow.after(300, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
   elif ImageStatisticsCreated==True and StepOfProcessCreation==2:
      StepOfProcessCreation+=1
      Widgets['TextFileIcon'].place(x=-400, y=-120, relx=0.5, rely=0.5, anchor='center')
      if int(IBNGWindow.winfo_width())<1100:
          Widgets['TextFileIcon'].place(x=65, y=-120, relx=0, rely=0.5, anchor='w')
      IBNGWindow.after(500, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
   elif ImageStatisticsCreated==True and StepOfProcessCreation==3:
      StepOfProcessCreation+=1
      Widgets['ImageStatisticsCreatedText'].place(x=-400, y=33, relx=0.5, rely=0.5, anchor='center')
      if int(IBNGWindow.winfo_width())<1100:
          Widgets['ImageStatisticsCreatedText'].place(x=18, y=33, relx=0, rely=0.5, anchor='w')
      Widgets['ProcessFilePlace2'].place(x=0, y=-120, relx=0.5, rely=0.5, anchor='center')
      IBNGWindow.after(500, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
   elif ImageStatisticsCreated==True and StepOfProcessCreation==4:
      StepOfProcessCreation+=1
      Widgets['ProcessIcon'].place(x=0, y=-120, relx=0.5, rely=0.5, anchor='center')
      ProcessThreading=threading.Thread(target=CreatePalette)
      ProcessThreading.start()
      IBNGWindow.after(200, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
   elif PaletteCreated==True and StepOfProcessCreation==5:
      StepOfProcessCreation+=1
      Widgets['ProcessIcon'].place_forget()
      IBNGWindow.after(300, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
   elif PaletteCreated==True and StepOfProcessCreation==6:
      StepOfProcessCreation+=1
      Widgets['PaletteCreateIcon'].place(x=0, y=-120, relx=0.5, rely=0.5, anchor='center')
      IBNGWindow.after(500, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
   elif PaletteCreated==True and StepOfProcessCreation==7:
      StepOfProcessCreation+=1
      Widgets['PaletteCreatedText'].place(x=0, y=33, relx=0.5, rely=0.5, anchor='center')
      Widgets['ProcessFilePlace3'].place(x=400, y=-120, relx=0.5, rely=0.5, anchor='center') 
      if int(IBNGWindow.winfo_width())<1100:
          Widgets['ProcessFilePlace3'].place(x=-19, y=-120, relx=1, rely=0.5, anchor='e')
      IBNGWindow.after(500, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
   elif PaletteCreated==True and StepOfProcessCreation==8:
      StepOfProcessCreation+=1
      ProccesIconPosition+=1
      Widgets['ProcessIcon'].place(x=400, y=-120, relx=0.5, rely=0.5, anchor='center')  
      if int(IBNGWindow.winfo_width())<1100:
          Widgets['ProcessIcon'].place(x=-79, y=-120, relx=1, rely=0.5, anchor='e')
      ProcessThreading=threading.Thread(target=CreateStockImageColor)
      ProcessThreading.start()
      IBNGWindow.after(200, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
   elif StockImageColorCreated==True and StepOfProcessCreation==9:
      StepOfProcessCreation+=1
      ProccesIconPosition+=1
      Widgets['ProcessIcon'].place_forget()
      IBNGWindow.after(300, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
   elif StockImageColorCreated==True and StepOfProcessCreation==10:
      StepOfProcessCreation+=1
      Widgets['ImageByColorFromStockIcon'].place(x=400, y=-120, relx=0.5, rely=0.5, anchor='center')
      if int(IBNGWindow.winfo_width())<1100:
          Widgets['ImageByColorFromStockIcon'].place(x=-65, y=-120, relx=1, rely=0.5, anchor='e')
      IBNGWindow.after(500, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
   elif StockImageColorCreated==True and StepOfProcessCreation==11:
      StepOfProcessCreation+=1
      Widgets['StockImageColorCreatedText'].place(x=400, y=33, relx=0.5, rely=0.5, anchor='center')
      if int(IBNGWindow.winfo_width())<1100:
          Widgets['StockImageColorCreatedText'].place(x=-12, y=33, relx=1, rely=0.5, anchor='e')
      Widgets['ProcessFilePlace4'].place(x=0, y=190, relx=0.5, rely=0.5, anchor='center')
      IBNGWindow.after(500, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
   elif StockImageColorCreated==True and StepOfProcessCreation==12:
      StepOfProcessCreation+=1
      Widgets['ProcessIcon'].place(x=0, y=190, relx=0.5, rely=0.5, anchor='center')
      ProcessThreading=threading.Thread(target=CreateImageByNumber)
      ProcessThreading.start()
      IBNGWindow.after(200, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
   elif ImageByNumberCreated==True and StepOfProcessCreation==13:
      StepOfProcessCreation+=1
      Widgets['ProcessIcon'].place_forget()
      IBNGWindow.after(300, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
   elif ImageByNumberCreated==True and StepOfProcessCreation==14:
      StepOfProcessCreation+=1
      Widgets['ImageByNumberIcon'].place(x=0, y=190, relx=0.5, rely=0.5, anchor='center')
      IBNGWindow.after(500, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
   elif ImageByNumberCreated==True and StepOfProcessCreation==15:
      StepOfProcessCreation+=1
      Widgets['ImageByNumberCreatedText'].place(x=0, y=343, relx=0.5, rely=0.5, anchor='center')
      if 'ImageByNumberCreatedText' in Widgets and Widgets['ImageByNumberCreatedText'].place_info() != {} and int(IBNGWindow.winfo_width())<725 and Widgets['ImageByNumberCreatedText'].place_info()['anchor']=='center':
            Widgets['ImageByNumberCreatedText'].place(x=-7, y=343, relx=0.5, rely=1, anchor='s')
      IBNGWindow.after(3000, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
   elif ImageByNumberCreated==True and StepOfProcessCreation==16:
      for WindowElement in IBNGWindow.winfo_children():
         WindowElement.destroy()
      IBNGWindow.resizable(True, True)
      OpenMainWindow()
   else:
      if 'ProcessIcon' in Widgets:
         Widgets['ProcessIcon'].update_idletasks()
         Widgets['ProcessIcon']['image']=TkImages['ProcessIconPart'+str(AnimationIcon)]
      if AnimationIcon==4:
         AnimationIcon+=1
         IBNGWindow.after(100, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
      elif AnimationIcon==8:
         AnimationIcon+=1
         IBNGWindow.after(100, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
      elif AnimationIcon==12:
         AnimationIcon+=1
         IBNGWindow.after(150, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
      elif AnimationIcon==16:
         AnimationIcon+=1
         IBNGWindow.after(100, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
      elif AnimationIcon==20:
         AnimationIcon+=1
         IBNGWindow.after(100, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
      elif AnimationIcon==24:
         AnimationIcon=1
         IBNGWindow.after(150, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)
      else:
         AnimationIcon+=1
         IBNGWindow.after(50, ProcessCreationIconAnimation, AnimationIcon, StepOfProcessCreation)








def CreateImageStatistics():
    global ColorsPercentInImageDeleteDublicates
    global EndColorsDeleteDublicates
    global ImageStatisticsCreated
    global FolderName
    try:
        FolderName=os.path.splitext(os.path.basename(SelectedImagePath))[0]
        FolderNameNumber=1
        while True:
            if not os.path.exists(ApplicationPath+f"/Cash/ResultsFiles/{FolderName+(str(FolderNameNumber) if FolderNameNumber>1 else '')}"):
                break
            else:
                FolderNameNumber+=1
                
        FolderName+=f'({str(FolderNameNumber)})' if FolderNameNumber>1 else ''
        os.mkdir(ApplicationPath+f"/Cash/ResultsFiles/{FolderName}") 
                
            

        
        ImageStatistic=''
        ImageStatistic+='RealColor-ColorFromStock, Percent:\n'
        EndColorsDeleteDublicates=[]
        ColorsPercentInImageDeleteDublicates=[]
        for ColorInRGB, ColorPercentInImage, EndColor in zip(ColorsInRGB, ColorsPercentInImage, EndColors):
            if EndColor not in EndColorsDeleteDublicates:
                EndColorsDeleteDublicates.append(EndColor)
                ColorsPercentInImageDeleteDublicates.append(ColorPercentInImage)
            else:
                ColorsPercentInImageDeleteDublicates[EndColorsDeleteDublicates.index(EndColor)]+=ColorPercentInImage
            
            ImageStatistic+=str(ColorsInRGB.index(ColorInRGB)+1)+')'+str(ColorInRGB)[0:-6]+') - '+str(EndColor)+', '+str(ColorPercentInImage)+'%'+'\n'




        ImageStatistic+='\nColorFromStockImage, Percent:\n'
        for IndexRealStockColorDeleteDublicates, (RealStockColorDeleteDublicates, ColorsPercentInImageDeleteDublicate) in enumerate(zip(EndColorsDeleteDublicates, ColorsPercentInImageDeleteDublicates)):
            ImageStatistic+=str(IndexRealStockColorDeleteDublicates+1)+')'+str(RealStockColorDeleteDublicates)+', '+str(ColorsPercentInImageDeleteDublicate)+'%'+'\n'

        time.sleep(3)

        with open(ApplicationPath+f"/Cash/ResultsFiles/{FolderName}/ImageStatistic.txt" ,"w", encoding='utf-8') as ImageStatisticFile:
            ImageStatisticFile.write(ImageStatistic)
            ImageStatisticFile.close()
        ImageStatisticsCreated=True
        time.sleep(1)
    except Exception as Error:
        IBNGExcepthook()




def CreatePalette():
   global PaletteCreated
   try:
       PaletteImageSize=1010*len(ColorsInRGB)-100
       if len(ColorsInRGB)<4:
          PaletteImageSize=3940
       PaletteImage=Image.new('RGBA', (PaletteImageSize, 3620), color = (255, 249, 233,255))
       DrawPaletteImage = ImageDraw.Draw(PaletteImage)

       DrawPaletteImage.text(((PaletteImage.size[0]-2282)//2, 78), 'Real Palette', font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 400), fill=(255, 173, 0, 255))
        
       for NumberOfColor, (ColorInRGB, ColorPercentInImage) in enumerate(zip(ColorsInRGB, ColorsPercentInImage)):
          ColorImage=Image.new('RGBA', (710, 710), color = (255, 255, 255,0))
          ColorImageDraw=ImageDraw.Draw(ColorImage)
          ColorImageDraw.rectangle([(30, 30), (675, 675)], fill=ColorInRGB)
          ColorImage.paste(Image.open(GetDataFilePath('English/PaletteColor.png')), (0, 0), mask=Image.open(GetDataFilePath('English/PaletteColor.png')))
          if len(str(NumberOfColor+1))==1:
             ColorImageDraw.text((90, 35), str(NumberOfColor+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))
          else:
             ColorImageDraw.text((30, 35), str(NumberOfColor+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))
             
          
          PaletteImage.paste(ColorImage, (1010*NumberOfColor+100, 700), mask=ColorImage)
          DrawPaletteImage.text((1010*NumberOfColor+({ (3, False): 198, (4, True): 176, (3, True): 226, (2, False): 254, (1, False): 309}.get((len(str(ColorPercentInImage)), '.' in str(ColorPercentInImage)), 0)), 1534), str(ColorPercentInImage)+'%', font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))


       DrawPaletteImage.text(((PaletteImage.size[0]-2192)//2, 1888), 'End Palette', font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 400), fill=(255, 173, 0, 255))

       for NumberOfColor, (EndColor, ColorPercentInImageDeleteDublicates) in enumerate(zip(EndColors, ColorsPercentInImageDeleteDublicates)):
          ColorImage=Image.new('RGBA', (710, 710), color = (255, 255, 255,0))
          ColorImageDraw=ImageDraw.Draw(ColorImage)
          ColorImageDraw.rectangle([(30, 30), (675, 675)], fill=EndColor)
          ColorImage.paste(Image.open(GetDataFilePath('English/PaletteRealStockColor.png')), (0, 0), mask=Image.open(GetDataFilePath('English/PaletteRealStockColor.png')))
          if len(str(NumberOfColor+1))==1:
             ColorImageDraw.text((90, 35), str(NumberOfColor+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))
          else:
             ColorImageDraw.text((30, 35), str(NumberOfColor+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))


          if len(str(ColorsStock.index(EndColor)+1))==1:
             ColorImageDraw.text((574, 544), str(ColorsStock.index(EndColor)+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 100), fill=(255, 173, 0, 255))
          else:
             ColorImageDraw.text((543, 544), str(ColorsStock.index(EndColor)+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 100), fill=(255, 173, 0, 255))

          
          PaletteImage.paste(ColorImage, (1010*NumberOfColor+100, 2510), mask=ColorImage)
          
          DrawPaletteImage.text((1010*NumberOfColor+({ (3, False): 198, (4, True): 176, (3, True): 226, (2, False): 254, (1, False): 309}.get((len(str(ColorPercentInImageDeleteDublicates)), '.' in str(ColorPercentInImageDeleteDublicates)), 0)), 3344), str(ColorPercentInImageDeleteDublicates)+'%', font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))

        
       PaletteImage.save(ApplicationPath+f'/Cash/ResultsFiles/{FolderName}/PalettesForImageByNumber.png')

       time.sleep(1)
        
       PaletteCreated=True
       time.sleep(1)
   except Exception as Error:
        IBNGExcepthook()



def CreateStockImageColor():
   global StockImageColorCreated
   try:
       StockImageColor = PillowImages['SelectedImage'].copy()
       StockImageColorPillowPixels=StockImageColor.load()
       StockImageColorNumpyPixels = np.array(StockImageColor)

       for ColorInRGB, EndColor in zip(ColorsInRGB, EndColors):
            for YNewColorImage, XNewColorImage in list(zip(*np.where(np.all(StockImageColorNumpyPixels == ColorInRGB, axis=-1)))):
                StockImageColorPillowPixels[XNewColorImage, YNewColorImage]=EndColor
        
       StockImageColor.save(ApplicationPath+f'/Cash/ResultsFiles/{FolderName}/StockImageColor.png')

       time.sleep(1)
       StockImageColorCreated=True
   except Exception as Error:
        IBNGExcepthook()






#CreateImageByNumber
def CreateImageByNumber():
    global ImageByNumberGeneratedLayer, ImageByNumberCreated, ContourImage, PartPixels, SelectedToChangeImage, PillowButtonContourImages, TkButtonContourImages, PillowButtonContourImageSettingsClamped, TkButtonContourImageSettingsClamped, PillowButtonContourImageConfigureContourImage, TkButtonContourImageConfigureContourImage
    try:
        Times.start()

        ContourImage=Image.new('RGBA', PillowImages['SelectedImage'].size, color = (255, 255, 255,0))
        ImageByNumber=ImageDraw.Draw(ContourImage)
        SelectedImageWidth, SelectedImageHeight=PillowImages['SelectedImage'].size
        AllowWidth, AllowHeight = int(SelectedImageWidth*0.2)+int(SelectedImageWidth*0.02), int(SelectedImageHeight*0.2)+int(SelectedImageHeight*0.02)
        SomeAllowWidth, SomeAllowHeight = int(SelectedImageWidth*0.2), int(SelectedImageHeight*0.2)

        #SplitByElement:
        def SplitByElement(SelectedToChangeImage, XPixel, YPixel):
            global PartPixels
            
            PixelsSelectedToChangeImage = SelectedToChangeImage.load()
            OriginalColor = PixelsSelectedToChangeImage[XPixel, YPixel]

            if OriginalColor == (0, 0, 0, 255):
                return

            Queue = deque([(XPixel, YPixel)])
            Visited = set([(XPixel, YPixel)])

            while Queue:
                XPixel, YPixel = Queue.popleft()

                if (
                    XPixel < 0
                    or XPixel >= SelectedImageWidth
                    or YPixel < 0
                    or YPixel >= SelectedImageHeight
                    or PixelsSelectedToChangeImage[XPixel, YPixel] != OriginalColor
                ):
                    continue

                PixelsSelectedToChangeImage[XPixel, YPixel] = (0, 0, 0, 255)
                PartPixels.append((XPixel, YPixel))
                Queue.extend((XPixel + dx, YPixel + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)])
                Visited.add((XPixel, YPixel))


                     
        #Set Numbers
        NumberColor=1
        for ColorInRGB in ColorsInRGB:
            start=time.time()
            NumberColor=int(EndColorsDeleteDublicates.index(EndColors[ColorsInRGB.index(ColorInRGB)])+1)
            FontContourImage = ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 10)
            NumberWidth=len(str(NumberColor))*3
            NumberHeight=6

            SelectedToChangeImage = PillowImages['SelectedImage'].copy()
            NumpySelectedToChangeImage = np.array(SelectedToChangeImage)

            NumpySelectedToChangeImage[np.any(NumpySelectedToChangeImage != ColorInRGB, axis=-1)] = [255, 255, 255, 0]

            SelectedToChangeImage = Image.fromarray(NumpySelectedToChangeImage).copy()
            PixelsSelectedToChangeImage = SelectedToChangeImage.load()

            SelectedByPartColor = Image.new('RGBA', SelectedToChangeImage.size, color = (255, 255, 255,0))
            PixelsSelectedByPartColor = SelectedByPartColor.load()

            
            while True:
                StartPixel=np.argwhere(np.any(NumpySelectedToChangeImage == np.array(ColorInRGB), axis=-1))
                SelectedToChangeImage.show()

                if len(StartPixel)==0:
                    break
                else:
                    StartPixel=tuple(StartPixel[0])
                    PartPixels = []
                    SplitByElement(SelectedToChangeImage, StartPixel[1], StartPixel[0])
                    if len(PartPixels)>25:
                        SelectedToChangeImage2 = Image.new('RGBA', SelectedToChangeImage.size, color = (255, 255, 255,0))
                        PixelsSelectedToChangeImage2 = SelectedToChangeImage2.load()
                        for PartPixel in PartPixels:
                            PixelsSelectedByPartColor[PartPixel[0], PartPixel[1]]=ColorInRGB
                            PixelsSelectedToChangeImage2[PartPixel[0], PartPixel[1]]=ColorInRGB

                        SelectedToChangeImage2.show()
                
                        NumpyPixelsSelectedToChangeImage = np.array(SelectedToChangeImage2)
                        AllX=np.where(NumpyPixelsSelectedToChangeImage[:, :, 3] == 255)[1].tolist()
                        AllY=np.where(NumpyPixelsSelectedToChangeImage[:, :, 3] == 255)[0].tolist()



                        def GetCenterY(CenterX):
                            AllYCenter = np.where(NumpyPixelsSelectedToChangeImage[:, CenterX, 3] == 255)[0].tolist()

                            AllowPlasesY=[]

                            MinY=min(AllYCenter)
                            MaxY=min(AllYCenter)
                            FindAllowPlace=True
                            for BrowseY in range(MinY, SelectedImageHeight):
                                if FindAllowPlace==True and PixelsSelectedToChangeImage[CenterX, BrowseY][3]==0 or FindAllowPlace==True and PixelsSelectedToChangeImage[CenterX, BrowseY][3]==255 and BrowseY==SelectedImageHeight-1:
                                    FindAllowPlace=False
                                    AllowPlasesY.append([MinY, BrowseY-1])
                                elif FindAllowPlace==False and PixelsSelectedToChangeImage[CenterX, BrowseY][3]==255:
                                    FindAllowPlace=True
                                    MinY = BrowseY


                                    

                            MinY=max(AllowPlasesY, key=lambda List:List[1]-List[0])[0]
                            MaxY=max(AllowPlasesY, key=lambda List:List[1]-List[0])[1]
                                    
                                
                            return int((MaxY-MinY)/2+MinY)




                    def GetCenterX(CenterY):
                        AllXCenter = np.where(NumpyPixelsSelectedToChangeImage[CenterY, :, 3] == 255)[0].tolist()

                        AllowPlasesX=[]

                        MinX=min(AllXCenter)
                        MaxX=min(AllXCenter)
                        FindAllowPlace=True

                        for BrowseX in range(MinX, SelectedImageWidth):
                            if FindAllowPlace==True and PixelsSelectedToChangeImage[BrowseX, CenterY][3]==0 or FindAllowPlace==True and PixelsSelectedToChangeImage[BrowseX, CenterY][3]==255 and BrowseX==SelectedImageWidth-1:
                                FindAllowPlace=False
                                AllowPlasesX.append([MinX, BrowseX-1])
                            elif FindAllowPlace==False and PixelsSelectedToChangeImage[BrowseX, CenterY][3]==255:
                                FindAllowPlace=True
                                MinX = BrowseX


                        MinX=max(AllowPlasesX, key=lambda List:List[1]-List[0])[0]
                        MaxX=max(AllowPlasesX, key=lambda List:List[1]-List[0])[1]
                                
                            
                        return int((MaxX-MinX)/2+MinX)





                    if max(AllX)-min(AllX)>max(AllY)-min(AllY):
                        if max(AllX)-min(AllX)<=AllowWidth:
                            CenterX=int((max(AllX)-min(AllX))/2+min(AllX))
                            EditCenterX=[]
                            EditCenterY=[]

                            while True:
                                CenterY=GetCenterY(CenterX)
                                CenterX=GetCenterX(CenterY)
                                
                                if CenterX in EditCenterX and CenterY in EditCenterY:
                                    break
                                else:
                                    EditCenterX.append(CenterX)
                                    EditCenterY.append(CenterY)
                            
                            ImageByNumber.text((CenterX-NumberWidth, CenterY-NumberHeight), str(NumberColor), font=FontContourImage, fill=(0, 0, 0, 255))
                        else:
                            for PrintNumberTime in range(1, math.floor((max(AllX)-min(AllX))/SomeAllowWidth)+1):
                                CenterX=PrintNumberTime*SomeAllowWidth+min(AllX)
                                StartCenterX=CenterX
                                EditCenterY=[]
                                
                                while True:
                                    CenterY=GetCenterY(CenterX)

                                    if CenterY in EditCenterY:
                                        break
                                    else:
                                        EditCenterY.append(CenterY)
                                
                                while CenterX<SelectedImageWidth and PixelsSelectedToChangeImage[CenterX, CenterY][3]!=255:
                                    CenterX+=1

                                if StartCenterX != CenterX:
                                    CenterX+=50
                                
                                ImageByNumber.text((CenterX-NumberWidth, CenterY-NumberHeight), str(NumberColor), font=FontContourImage, fill=(0, 0, 0, 255))

                    else:
                        if max(AllY)-min(AllY)<=AllowHeight:
                            
                            CenterY=int((max(AllY)-min(AllY))/2+min(AllY))
                            EditCenterX=[]
                            EditCenterY=[]

                            while True:
                                CenterX=GetCenterX(CenterY)
                                CenterY=GetCenterY(CenterX)
                                
                                if CenterX in EditCenterX and CenterY in EditCenterY:
                                    break
                                else:
                                    EditCenterX.append(CenterX)
                                    EditCenterY.append(CenterY)
                            
                            ImageByNumber.text((CenterX-NumberWidth, CenterY-NumberHeight), str(NumberColor), font=FontContourImage, fill=(0, 0, 0, 255))
                            
                        else:
                            for PrintNumberTime in range(1, math.floor((max(AllY)-min(AllY))/SomeAllowHeight)+1):
                                CenterY=PrintNumberTime*SomeAllowHeight+min(AllY)
                                StartCenterY=CenterY
                                EditCenterX=[]

                                while True:
                                    CenterX=GetCenterX(CenterY)
                                    
                                    if CenterX in EditCenterX:
                                        break
                                    else:
                                        EditCenterX.append(CenterX)
                                
                                while CenterY<SelectedImageHeight and PixelsSelectedToChangeImage[CenterX, CenterY][3]!=255:
                                    CenterY+=1

                                if StartCenterY != CenterY:
                                    CenterY+=50
                                
                                ImageByNumber.text((CenterX-NumberWidth, CenterY-NumberHeight), str(NumberColor), font=FontContourImage, fill=(0, 0, 0, 255))

                    
                for PartPixel in PartPixels:
                    PixelsSelectedToChangeImage[PartPixel[0], PartPixel[1]]=(255, 255, 255, 0)


            print(time.time()-start)
                        
            SelectedByPartColorNumpy = np.array(SelectedByPartColor)
            ColorRegion = np.all(SelectedByPartColorNumpy == ColorInRGB, axis=2)

            ColorRegionPadded = np.pad(ColorRegion, ((1, 1), (1, 1)), mode='constant')

            Contours = (ColorRegionPadded[:-2, 1:-1] != ColorRegionPadded[2:, 1:-1]) | (ColorRegionPadded[1:-1, :-2] != ColorRegionPadded[1:-1, 2:])

            ContoursY, ContoursX = np.where(Contours==True)

            Contours = list(zip(ContoursX, ContoursY))
            
            for Contour in Contours:
                ImageByNumber.point(Contour, fill=(0, 0, 0))

            ContourImage.save(ApplicationPath+f'/Cash/ResultsFiles/{FolderName}/ImageByNumber.png')
            ImageByNumberGeneratedLayer=ColorsInRGB.index(ColorInRGB)+1
            print(ImageByNumberGeneratedLayer)

        ContourImage.save(ApplicationPath+f'/Cash/ResultsFiles/{FolderName}/ImageByNumber.png')


        SelectedImage=PillowImages['SelectedImage'].convert("RGBA")
        SelectedImageSize=SelectedImage.size


        if SelectedImageSize[0]>SelectedImageSize[1]:
            Width=int(SelectedImageSize[0]/SelectedImageSize[1]*200)
            SelectedImage=SelectedImage.resize((Width, 200))
            SelectedImage=SelectedImage.crop(((Width // 2)-94, 6, (Width // 2), 194))
        else:
            Height=int(SelectedImageSize[1]/SelectedImageSize[0]*200)#200
            SelectedImage=SelectedImage.resize((200, Height))
            SelectedImage=SelectedImage.crop((6, ((Height // 2)-94), 100, ((Height // 2)+94)))

        ContourImage=ContourImage.convert("RGBA")
        ContourImageSize=ContourImage.size

        if ContourImageSize[0]>ContourImageSize[1]:
            Width=int(ContourImageSize[0]/ContourImageSize[1]*200)
            ContourImage=ContourImage.resize((Width, 200))
            ContourImage=ContourImage.crop(((Width // 2), 6, (Width // 2)+94, 194))
        else:
            Height=int(ContourImageSize[1]/ContourImageSize[0]*200)
            ContourImage=ContourImage.resize((200, Height))
            ContourImage=ContourImage.crop((100, ((Height // 2)-94), 194, ((Height // 2)+94)))

        ButtonContourImage=Image.new('RGBA', (200, 200), color = (255, 255, 255, 0))
        ButtonContourImageDraw=ImageDraw.Draw(ButtonContourImage)
        ButtonContourImageDraw.rectangle([(7,7), (193, 193)], fill=(255, 255, 255, 255))
        ButtonContourImage.paste(SelectedImage, (6, 6), SelectedImage)
        ButtonContourImage.paste(ContourImage, (100, 6), ContourImage)
        ButtonContourImage.paste(Image.open(GetDataFilePath('English/ContourButtonField.png')), (0, 0), mask=Image.open(GetDataFilePath('English/ContourButtonField.png')))
        ButtonContourImageSettingsClamped=ButtonContourImage.copy()
        ButtonContourImage.paste(Image.open(GetDataFilePath('English/SettingsButtonContourImage.png')), (140, 178), mask=Image.open(GetDataFilePath('English/SettingsButtonContourImage.png')))
        ButtonContourImageSettingsClamped.paste(Image.open(GetDataFilePath('English/SettingsButtonContourImageClamped.png')), (140, 178), mask=Image.open(GetDataFilePath('English/SettingsButtonContourImageClamped.png')))
        ButtonContourImageConfigureContourImage=ButtonContourImage.copy()
        ButtonContourImageConfigureContourImage.paste(Image.open(GetDataFilePath('English/ConfigureContourImageBackground.png')), (0, 0), mask=Image.open(GetDataFilePath('English/ConfigureContourImageBackground.png')))
        ButtonContourImage.save(ApplicationPath+f'/Cash/ResultsFiles/{FolderName}/ButtonContourImage.png')
        ButtonContourImageSettingsClamped.save(ApplicationPath+f'/Cash/ResultsFiles/{FolderName}/ButtonContourImageSettingsClamped.png')
        ButtonContourImageConfigureContourImage.save(ApplicationPath+f'/Cash/ResultsFiles/{FolderName}/ButtonContourImageConfigureContourImage.png')


            
        PillowButtonContourImages = []
        TkButtonContourImages = []
        PillowButtonContourImageSettingsClamped = []
        TkButtonContourImageSettingsClamped = []
        PillowButtonContourImageConfigureContourImage = []
        TkButtonContourImageConfigureContourImage = []
        CreatedImages=[ResultImage for ResultImage in os.listdir(ApplicationPath+'/Cash/ResultsFiles') if os.path.isdir(os.path.join(ApplicationPath+'/Cash/ResultsFiles', ResultImage))]
        CreatedImages = sorted(CreatedImages, key=lambda File: os.stat(ApplicationPath+'/Cash/ResultsFiles/'+File).st_birthtime, reverse=True)
        for CreatedImageNumber, CreatedImage in enumerate(CreatedImages):
            if len(os.listdir(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage))<5:
                if os.path.exists(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage):
                    shutil.rmtree(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage)
            else:
                CreatedImageSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12).getbbox(CreatedImage)
                CreatedImageSize=CreatedImageSize[2]-CreatedImageSize[0]
                if CreatedImageSize<133:
                    CreatedImageText=CreatedImage
                else:
                    CreatedImageText=CreatedImage
                    while CreatedImageSize>=133:
                        CreatedImageSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12).getbbox(CreatedImageText+'...')
                        CreatedImageSize=CreatedImageSize[2]-CreatedImageSize[0]
                        CreatedImageText=CreatedImageText[:-1]
                    CreatedImageText+='...'
                PillowButtonContourImages.append(Image.open(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage+'/ButtonContourImage.png'))
                PillowButtonContourImagesDraw=ImageDraw.Draw(PillowButtonContourImages[-1])
                PillowButtonContourImagesDraw.text((9, 176), CreatedImageText, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12), fill=(255, 176, 0, 255))
                TkButtonContourImages.append(ImageTk.PhotoImage(PillowButtonContourImages[-1]))
                PillowButtonContourImageSettingsClamped.append(Image.open(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage+'/ButtonContourImageSettingsClamped.png'))
                PillowButtonContourImageSettingsClampedDraw=ImageDraw.Draw(PillowButtonContourImageSettingsClamped[-1])
                PillowButtonContourImageSettingsClampedDraw.text((9, 176), CreatedImageText, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12), fill=(255, 176, 0, 255))
                TkButtonContourImageSettingsClamped.append(ImageTk.PhotoImage(PillowButtonContourImageSettingsClamped[-1]))
                PillowButtonContourImageConfigureContourImage.append(Image.open(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage+'/ButtonContourImageConfigureContourImage.png'))
                PillowButtonContourImageConfigureContourImageDraw=ImageDraw.Draw(PillowButtonContourImageConfigureContourImage[-1])
                PillowButtonContourImageConfigureContourImageDraw.text((9, 176), CreatedImageText, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12), fill=(255, 176, 0, 255))
                TkButtonContourImageConfigureContourImage.append(ImageTk.PhotoImage(PillowButtonContourImageConfigureContourImage[-1]))
            
        IBNGWindow.resizable(False, False)
        def EndFunction():
            global ImageByNumberCreated
            ImageByNumberCreated=True
        IBNGWindow.after(100, EndFunction)
        Times.stop()      

    except Exception as Error:
        traceback.print_exc() 
        IBNGExcepthook()


































def ContourImageNumberButtonsOnClick(Event):
    global SettingsIsClicked
    if Event.x in [AvailableX for AvailableX in range(141, 180)] and Event.y in [AvailableY for AvailableY in range(179, 188)]:
        Event.widget['image']=TkButtonContourImageSettingsClamped[ContourImageNumberButtons.index(Event.widget)]
        SettingsIsClicked=True
    elif Event.x>=0 and Event.y>=0 and Event.x<=200 and Event.y<=200:
        def ContourImageNumberButtonsEnterAnimate(Width, Height):
            global TkButtonContourImages
            if Width > 196:
                Width -= 2
                Height -= 2
                ButtonContourImageNew=Image.new('RGBA', (200, 200), color = (255, 255, 255, 0))
                ButtonContourImageOld=PillowButtonContourImages[ContourImageNumberButtons.index(Event.widget)].resize((Width, Height))
                ButtonContourImageNew.paste(ButtonContourImageOld, ((200-Width)//2, (200-Height)//2), ButtonContourImageOld)
                TkButtonContourImages[ContourImageNumberButtons.index(Event.widget)] = ImageTk.PhotoImage(ButtonContourImageNew)
                Event.widget['image'] = TkButtonContourImages[ContourImageNumberButtons.index(Event.widget)]
                IBNGWindow.after(1, ContourImageNumberButtonsEnterAnimate, Width, Height)
        ContourImageNumberButtonsEnterAnimate(200, 200)



def ContourImageNumberButtonsRealese(Event):
    global SettingsIsClicked
    global IsEnterRenameButtonContourImage
    global IsEnterDeleteButtonContourImage
    global TkButtonContourImages
    if Event.x in [AvailableX for AvailableX in range(141, 180)] and Event.y in [AvailableY for AvailableY in range(179, 188)]:
        IBNGWindow['bg']="#ffdaaf"
        [WindowElement.unbind(Event2) for WindowElement in IBNGWindow.winfo_children() for Event2 in Bindings]
        [IBNGWindow.unbind_all(Event2) for Event2 in Bindings]
        [WindowElement.unbind(Event2) for WindowElement in ScrollFrame.winfo_children() for Event2 in Bindings]

        Widgets['BackgroundDetail1']['image']=TkImages['BackgroundDetail1ConfigureContourImage']
        Widgets['BackgroundDetail2']['image']=TkImages['BackgroundDetail2ConfigureContourImage']
        Widgets['IBNGTextIcon']['image']=TkImages['IBNGTextIconConfigureContourImage']
        Widgets['IBNGTextIcon']['bg']="#ffdaaf"
        Widgets['YourContentText']['image']=TkImages['YourContentTextConfigureContourImage']
        Widgets['YourContentText']['bg']="#ffd8a3"
        Widgets['SettingsButton']['image']=TkImages['SettingsButtonConfigureContourImage']
        Widgets['SettingsButton']['bg']="#ffdaaf"
        Widgets['StartCreatingButton']['image']=TkImages['StartCreatingButtonConfigureContourImage']
        ScrollCanvas['bg']="#ffdaaf"
        ScrollCanvas['highlightbackground']="#ffdaaf"
        ScrollFrame['bg']="#ffdaaf"
        for ContourImageNumberButton in ContourImageNumberButtons:
            ContourImageNumberButton['bg']="#ffdaaf"
            if ContourImageNumberButton != Event.widget:
                ContourImageNumberButton['image']=TkButtonContourImageConfigureContourImage[ContourImageNumberButtons.index(ContourImageNumberButton)]

        
        Widgets['BackgroundDetail4'].place(relx=0.5, rely=1, anchor='s')
        Widgets['BackgroundDetail4'].lift()


        Widgets['RenameButtonContourImage'].place(x=-150, y=-15, relx=0.5, rely=1, anchor='s')
        Widgets['RenameButtonContourImage'].lift()
        Widgets['RenameButtonContourImage'].update()
        IsEnterRenameButtonContourImage=False

        Widgets['RenameButtonContourImage'].bind('<Enter>', RenameButtonContourImageOnEnter)
        Widgets['RenameButtonContourImage'].bind('<Leave>', RenameButtonContourImageOnLeave)
        Widgets['RenameButtonContourImage'].bind("<Button-1>", RenameButtonContourImageOnClick)
        Widgets['RenameButtonContourImage'].bind("<ButtonRelease-1>", lambda EventRenameButtonContourImage:RenameButtonContourImageRelease(EventRenameButtonContourImage, Event.widget))


        Widgets['DeleteButtonContourImage'].place(x=150, y=-15, relx=0.5, rely=1, anchor='s')
        Widgets['DeleteButtonContourImage'].lift()
        Widgets['DeleteButtonContourImage'].update()
        IsEnterDeleteButtonContourImage=False

        Widgets['DeleteButtonContourImage'].bind('<Enter>', DeleteButtonContourImageOnEnter)
        Widgets['DeleteButtonContourImage'].bind('<Leave>', DeleteButtonContourImageOnLeave)
        Widgets['DeleteButtonContourImage'].bind("<Button-1>", DeleteButtonContourImageOnClick)
        Widgets['DeleteButtonContourImage'].bind("<ButtonRelease-1>", lambda EventDeleteButtonContourImageRelease:DeleteButtonContourImageRelease(EventDeleteButtonContourImageRelease, Event.widget))

        def CloseConfigureContourImageReleased(EventCloseConfigureContourImageReleased):
            if EventCloseConfigureContourImageReleased.widget!=Event.widget and EventCloseConfigureContourImageReleased.widget!=Widgets['BackgroundDetail4'] and EventCloseConfigureContourImageReleased.widget!=Widgets['RenameButtonContourImage'] and EventCloseConfigureContourImageReleased.widget!=Widgets['DeleteButtonContourImage']:
                CloseConfigureContourImage(EventCloseConfigureContourImageReleased)
        IBNGWindow.bind('<ButtonRelease-1>', CloseConfigureContourImageReleased)
            

    elif Event.x>=0 and Event.y>=0 and Event.x<=200 and Event.y<=200 and SettingsIsClicked==False:
        def ContourImageNumberButtonsEnterAnimate(Width, Height):
            global TkButtonContourImages
            if Width < 200:
                Width += 2
                Height += 2
                ButtonContourImageNew=Image.new('RGBA', (200, 200), color = (255, 255, 255, 0))
                ButtonContourImageOld=PillowButtonContourImages[ContourImageNumberButtons.index(Event.widget)].resize((Width, Height))
                ButtonContourImageNew.paste(ButtonContourImageOld, ((200-Width)//2, (200-Height)//2), ButtonContourImageOld)
                if Width==200:
                   TkButtonContourImages[ContourImageNumberButtons.index(Event.widget)]=ImageTk.PhotoImage(PillowButtonContourImages[ContourImageNumberButtons.index(Event.widget)])
                Event.widget['image'] = TkButtonContourImages[ContourImageNumberButtons.index(Event.widget)]
                IBNGWindow.after(1, ContourImageNumberButtonsEnterAnimate, Width, Height)
            else:
                def GoToAnotherPage():
                    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
                    [IBNGWindow.unbind_all(Event) for Event in Bindings]
                    [IBNGWindow.unbind(Event) for Event in Bindings]
                    for WindowElement in IBNGWindow.winfo_children():
                       WindowElement.destroy()
                    OpenShowResultFile(ContourImageNumberButtons.index(Event.widget))
                IBNGWindow.after(100, GoToAnotherPage)
                
        ContourImageNumberButtonsEnterAnimate(196, 196)
    else:
        def ContourImageNumberButtonsEnterAnimate(Width, Height):
            global TkButtonContourImages
            if Width < 200:
                Width += 2
                Height += 2
                ButtonContourImageNew=Image.new('RGBA', (200, 200), color = (255, 255, 255, 0))
                ButtonContourImageOld=PillowButtonContourImages[ContourImageNumberButtons.index(Event.widget)].resize((Width, Height))
                ButtonContourImageNew.paste(ButtonContourImageOld, ((200-Width)//2, (200-Height)//2), ButtonContourImageOld)
                if Width==200:
                   TkButtonContourImages[ContourImageNumberButtons.index(Event.widget)]=ImageTk.PhotoImage(PillowButtonContourImages[ContourImageNumberButtons.index(Event.widget)])
                Event.widget['image'] = TkButtonContourImages[ContourImageNumberButtons.index(Event.widget)]
                IBNGWindow.after(1, ContourImageNumberButtonsEnterAnimate, Width, Height)
        if SettingsIsClicked==False:
            ContourImageNumberButtonsEnterAnimate(196, 196)
        else:
            TkButtonContourImages[ContourImageNumberButtons.index(Event.widget)]=ImageTk.PhotoImage(PillowButtonContourImages[ContourImageNumberButtons.index(Event.widget)])
            Event.widget['image'] = TkButtonContourImages[ContourImageNumberButtons.index(Event.widget)]
        
    SettingsIsClicked=False








def DeleteButtonContourImageOnClick(Event):
    Widgets['DeleteButtonContourImage']['image'] = TkImages['DeleteButtonContourImageClamped']


def DeleteButtonContourImageRelease(Event, Widget):
    Widgets['DeleteButtonContourImage']['image'] = TkImages['DeleteButtonContourImageRealesed']
    if IsEnterDeleteButtonContourImage == True:
        def GoToAnotherPage():
            global PillowButtonContourImages
            global TkButtonContourImages
            global PillowButtonContourImageSettingsClamped
            global TkButtonContourImageSettingsClamped
            global PillowButtonContourImageConfigureContourImage
            global TkButtonContourImageConfigureContourImage
            CreatedImages=[ResultImage for ResultImage in os.listdir(ApplicationPath+'/Cash/ResultsFiles') if os.path.isdir(os.path.join(ApplicationPath+'/Cash/ResultsFiles', ResultImage))]
            CreatedImages = sorted(CreatedImages, key=lambda File: os.stat(ApplicationPath+'/Cash/ResultsFiles/'+File).st_birthtime, reverse=True)
            CreatedImage=CreatedImages[ContourImageNumberButtons.index(Widget)]
            if os.path.exists(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage):
                shutil.rmtree(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage)
            ContourImageIndex=ContourImageNumberButtons.index(Widget)
            PillowButtonContourImages=PillowButtonContourImages[:ContourImageIndex]+PillowButtonContourImages[ContourImageIndex+1:]
            TkButtonContourImages=TkButtonContourImages[:ContourImageIndex]+TkButtonContourImages[ContourImageIndex+1:]
            PillowButtonContourImageSettingsClamped=PillowButtonContourImageSettingsClamped[:ContourImageIndex]+PillowButtonContourImageSettingsClamped[ContourImageIndex+1:]
            TkButtonContourImageSettingsClamped=TkButtonContourImageSettingsClamped[:ContourImageIndex]+TkButtonContourImageSettingsClamped[ContourImageIndex+1:]
            PillowButtonContourImageConfigureContourImage=PillowButtonContourImageConfigureContourImage[:ContourImageIndex]+PillowButtonContourImageConfigureContourImage[ContourImageIndex+1:]
            TkButtonContourImageConfigureContourImage=TkButtonContourImageConfigureContourImage[:ContourImageIndex]+TkButtonContourImageConfigureContourImage[ContourImageIndex+1:]

            CloseConfigureContourImage(Event)
        IBNGWindow.after(100, GoToAnotherPage)
        


def DeleteButtonContourImageOnEnter(Event):
   global IsEnterDeleteButtonContourImage
   IsEnterDeleteButtonContourImage=True

def DeleteButtonContourImageOnLeave(Event):
   global IsEnterDeleteButtonContourImage
   IsEnterDeleteButtonContourImage=False



   



def RenameButtonContourImageOnClick(Event):
    Widgets['RenameButtonContourImage']['image'] = TkImages['RenameButtonContourImageClamped']


def RenameButtonContourImageRelease(Event, Widget):
    Widgets['RenameButtonContourImage']['image'] = TkImages['RenameButtonContourImageRealesed']
    if IsEnterRenameButtonContourImage == True:
        def GoToAnotherPage():
            global IsEnterCancelRenameButton
            global IsEnterAcceptButton
            global RenameEntry
            Widgets['BackgroundDetail4'].place_forget()
            Widgets['RenameButtonContourImage'].place_forget()
            Widgets['DeleteButtonContourImage'].place_forget()


            
            Widgets['BackgroundDetail5'].place(relx=0.5, rely=1, anchor='s')
            Widgets['BackgroundDetail5'].lift()

            
            Widget['image']=TkButtonContourImageConfigureContourImage[ContourImageNumberButtons.index(Widget)]
            IBNGWindow.unbind('<ButtonRelease-1>')
            
            Widgets['CancelRenameButton']['image']=TkImages['CancelRenameButtonRealesed']
            Widgets['CancelRenameButton'].place(x=-300, y=-42, relx=0.5, rely=1, anchor='s')
            Widgets['CancelRenameButton'].lift()
            IsEnterCancelRenameButton=False

            Widgets['CancelRenameButton'].bind('<Enter>', CancelRenameButtonOnEnter)
            Widgets['CancelRenameButton'].bind('<Leave>', CancelRenameButtonOnLeave)
            Widgets['CancelRenameButton'].bind("<Button-1>", CancelRenameButtonOnClick)
            Widgets['CancelRenameButton'].bind("<ButtonRelease-1>", CancelRenameButtonRelease)
            
            
            Widgets['AcceptButton']['image']=TkImages['AcceptButtonRealesed']
            Widgets['AcceptButton'].place(y=-32, relx=0.5, rely=1, anchor='s')
            Widgets['AcceptButton'].lift()
            IsEnterAcceptButton=False

            Widgets['AcceptButton'].bind('<Enter>', AcceptButtonOnEnter)
            Widgets['AcceptButton'].bind('<Leave>', AcceptButtonOnLeave)
            Widgets['AcceptButton'].bind("<Button-1>", AcceptButtonOnClick)
            Widgets['AcceptButton'].bind("<ButtonRelease-1>", lambda EventAcceptButtonRelease:AcceptButtonRelease(EventAcceptButtonRelease, Widget))

            
            def CenterText(Event):
                CursorPosition = RenameEntry.index("insert")
                RenameEntryText = RenameEntry.get("1.0", "end-1c")
                RenameEntry.delete("1.0", "end")
                RenameEntry.insert("1.0", RenameEntryText, "center")
                RenameEntry.tag_add("centred", "1.0", "end")
                RenameEntry.mark_set("insert", CursorPosition)

                
            RenameEntry = Text(IBNGWindow, font="Arial 40", height=2, width=25, wrap="word", bg="#fff4d4", borderwidth=0, highlightthickness=3, highlightbackground='#ff9f0d', highlightcolor='#ff9f0d', fg='#fdb84e', insertbackground='#fdb84e')
            RenameEntry.place(relx=0.5, rely=0.5, anchor='center')
            RenameEntry.tag_configure("centred", justify='center')
            CreatedImages=[ResultImage for ResultImage in os.listdir(ApplicationPath+'/Cash/ResultsFiles') if os.path.isdir(os.path.join(ApplicationPath+'/Cash/ResultsFiles', ResultImage))]
            CreatedImages = sorted(CreatedImages, key=lambda File: os.stat(ApplicationPath+'/Cash/ResultsFiles/'+File).st_birthtime, reverse=True)
            RenameEntry.insert("1.0", CreatedImages[ContourImageNumberButtons.index(Widget)])
            RenameEntry.tag_add("centred", "1.0", "end")

            RenameEntry.bind("<KeyRelease>", CenterText)

            
        IBNGWindow.after(100, GoToAnotherPage)
        
   


def RenameButtonContourImageOnEnter(Event):
   global IsEnterRenameButtonContourImage
   IsEnterRenameButtonContourImage=True

def RenameButtonContourImageOnLeave(Event):
   global IsEnterRenameButtonContourImage
   IsEnterRenameButtonContourImage=False




def CancelRenameButtonOnClick(Event):
    Widgets['CancelRenameButton']['image'] = TkImages['CancelRenameButtonClamped']


def CancelRenameButtonRelease(Event):
    Widgets['CancelRenameButton']['image'] = TkImages['CancelRenameButtonRealesed']
    if IsEnterRenameButtonContourImage == True:
        def GoToAnotherPage():
            CloseConfigureContourImage(Event)

            
        IBNGWindow.after(100, GoToAnotherPage)
        
   


def CancelRenameButtonOnEnter(Event):
   global IsEnterRenameButtonContourImage
   IsEnterRenameButtonContourImage=True

def CancelRenameButtonOnLeave(Event):
   global IsEnterRenameButtonContourImage
   IsEnterRenameButtonContourImage=False






def AcceptButtonOnClick(Event):
    Widgets['AcceptButton']['image'] = TkImages['AcceptButtonClamped']


def AcceptButtonRelease(Event, Widget):
    Widgets['AcceptButton']['image'] = TkImages['AcceptButtonRealesed']
    if IsEnterAcceptButton == True:
        def GoToAnotherPage():
            import datetime
            RenameText=RenameEntry.get("1.0", "end-1c")
            CreatedImages=[ResultImage for ResultImage in os.listdir(ApplicationPath+'/Cash/ResultsFiles') if os.path.isdir(os.path.join(ApplicationPath+'/Cash/ResultsFiles', ResultImage))]
            CreatedImages = sorted(CreatedImages, key=lambda File: os.stat(ApplicationPath+'/Cash/ResultsFiles/'+File).st_birthtime, reverse=True)
            CreatedImage=CreatedImages[ContourImageNumberButtons.index(Widget)]

            if RenameText.replace(' ', '')=='':
                RenameText=CreatedImage
            elif RenameText != CreatedImage:
                RenameTextNumber=1
                while True:
                    if not os.path.exists(ApplicationPath+f"/Cash/ResultsFiles/{RenameText+(str(RenameTextNumber) if RenameTextNumber>1 else '')}"):
                        break
                    else:
                        RenameTextNumber+=1
                RenameText+=f'({str(RenameTextNumber)})' if RenameTextNumber>1 else ''
                ContourButtonIndex=ContourImageNumberButtons.index(Widget)
                if os.path.exists(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage):
                    shutil.move(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage, ApplicationPath+'/Cash/ResultsFiles/'+RenameText)

                CreatedImageSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12).getbbox(RenameText)
                CreatedImageSize=CreatedImageSize[2]-CreatedImageSize[0]
                if CreatedImageSize<133:
                    CreatedImageText=RenameText
                else:
                    CreatedImageText=RenameText
                    while CreatedImageSize>=133:
                        CreatedImageSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12).getbbox(CreatedImageText+'...')
                        CreatedImageSize=CreatedImageSize[2]-CreatedImageSize[0]
                        CreatedImageText=CreatedImageText[:-1]
                    CreatedImageText+='...'
                CreatedImages=[ResultImage for ResultImage in os.listdir(ApplicationPath+'/Cash/ResultsFiles') if os.path.isdir(os.path.join(ApplicationPath+'/Cash/ResultsFiles', ResultImage))]
                CreatedImages = sorted(CreatedImages, key=lambda File: os.stat(ApplicationPath+'/Cash/ResultsFiles/'+File).st_birthtime, reverse=True)
                PillowButtonContourImages[ContourButtonIndex]=Image.open(ApplicationPath+'/Cash/ResultsFiles/'+RenameText+'/ButtonContourImage.png')
                PillowButtonContourImagesDraw=ImageDraw.Draw(PillowButtonContourImages[ContourButtonIndex])
                PillowButtonContourImagesDraw.text((9, 176), CreatedImageText, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12), fill=(255, 176, 0, 255))
                TkButtonContourImages[ContourButtonIndex]=ImageTk.PhotoImage(PillowButtonContourImages[ContourButtonIndex])
                PillowButtonContourImageSettingsClamped[ContourButtonIndex]=Image.open(ApplicationPath+'/Cash/ResultsFiles/'+RenameText+'/ButtonContourImageSettingsClamped.png')
                PillowButtonContourImageSettingsClampedDraw=ImageDraw.Draw(PillowButtonContourImageSettingsClamped[ContourButtonIndex])
                PillowButtonContourImageSettingsClampedDraw.text((9, 176), CreatedImageText, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12), fill=(255, 176, 0, 255))
                TkButtonContourImageSettingsClamped[ContourButtonIndex]=ImageTk.PhotoImage(PillowButtonContourImageSettingsClamped[ContourButtonIndex])
                PillowButtonContourImageConfigureContourImage[ContourButtonIndex]=Image.open(ApplicationPath+'/Cash/ResultsFiles/'+RenameText+'/ButtonContourImageConfigureContourImage.png')
                PillowButtonContourImageConfigureContourImageDraw=ImageDraw.Draw(PillowButtonContourImageConfigureContourImage[ContourButtonIndex])
                PillowButtonContourImageConfigureContourImageDraw.text((9, 176), CreatedImageText, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12), fill=(255, 176, 0, 255))
                TkButtonContourImageConfigureContourImage[ContourButtonIndex]=ImageTk.PhotoImage(PillowButtonContourImageConfigureContourImage[ContourButtonIndex])

            
            CloseConfigureContourImage(Event)
            
        IBNGWindow.after(100, GoToAnotherPage)
        
   


def AcceptButtonOnEnter(Event):
   global IsEnterAcceptButton
   IsEnterAcceptButton=True

def AcceptButtonOnLeave(Event):
   global IsEnterAcceptButton
   IsEnterAcceptButton=False







def CloseConfigureContourImage(Event):
    IBNGWindow['bg']="#fff9e9"
    IBNGWindow.unbind('<ButtonRelease-1>')
    OpenMainWindow()














def TextFileButtonOnClick(Event):
    def TextFileButtonEnterAnimate(Width, Height):
        if Width > 250:
            Width -= 2
            Height -= 2
            TextFileResultFileButton=Image.new('RGBA', (260, 260), color = (255, 255, 255, 0))
            TextFileResultFileButtonOld=PillowImages['TextFileResultFileIcon'].resize((Width, Height))
            TextFileResultFileButton.paste(TextFileResultFileButtonOld, ((260-Width)//2, (260-Height)//2), TextFileResultFileButtonOld)
            TkImages['TextFileResultFileIcon'] = ImageTk.PhotoImage(TextFileResultFileButton)
            Widgets['TextFileResultFileIcon']['image'] = TkImages['TextFileResultFileIcon']
            IBNGWindow.after(1, TextFileButtonEnterAnimate, Width, Height)
    TextFileButtonEnterAnimate(260, 260)

def TextFileButtonRelease(Event, ContourButtonIndex):
    def TextFileButtonEnterAnimate(Width, Height):
        global IsEnterTextFileButton
        if Width < 260:
            Width += 2
            Height += 2
            TextFileResultFileButton=Image.new('RGBA', (260, 260), color = (255, 255, 255, 0))
            TextFileResultFileButtonOld=PillowImages['TextFileResultFileIcon'].resize((Width, Height))
            TextFileResultFileButton.paste(TextFileResultFileButtonOld, ((260-Width)//2, (260-Height)//2), TextFileResultFileButtonOld)
            TkImages['TextFileResultFileIcon'] = ImageTk.PhotoImage(TextFileResultFileButton)
            Widgets['TextFileResultFileIcon']['image'] = TkImages['TextFileResultFileIcon']
            IBNGWindow.after(1, TextFileButtonEnterAnimate, Width, Height)
        else:
            if IsEnterTextFileButton == True:
                def GoToAnotherPage():
                    IsEnterTextFileButton=False
                    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
                    [IBNGWindow.unbind_all(Event) for Event in Bindings]
                    [IBNGWindow.unbind(Event) for Event in Bindings]
                    for WindowElement in IBNGWindow.winfo_children():
                       WindowElement.destroy()
                    OpenShowTextFileButton(ContourButtonIndex)
                IBNGWindow.after(100, GoToAnotherPage)
    TextFileButtonEnterAnimate(250, 250)
   


def TextFileButtonOnEnter(Event):
   global IsEnterTextFileButton
   IsEnterTextFileButton=True

   
def TextFileButtonOnLeave(Event):
   global IsEnterTextFileButton
   IsEnterTextFileButton=False





def OpenShowTextFileButton(ContourButtonIndex):
    global StatistiTextFile
    global Widgets
    global StatistiText
    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
    [IBNGWindow.unbind_all(Event) for Event in Bindings]
    [IBNGWindow.unbind(Event) for Event in Bindings]
    for WindowElement in IBNGWindow.winfo_children():
       WindowElement.destroy()
    WidgetsInWindow = ['BackgroundDetail3', 'BackButton', 'DownloadButton', 'StatisticUploadedIcon']
    Widgets = {WidgetInformation[0]: Label(IBNGWindow, image=WidgetInformation[1], bg="#"+WidgetInformation[2], bd=0) for WidgetInformation in WidgetsInformation if WidgetInformation[0] in WidgetsInWindow}

    IBNGWindow.update()


    
    Widgets['BackgroundDetail3'].place(y=0, rely=0, relx=0.5, anchor='n')


    TextFileText=Label(IBNGWindow, text="Image Statistic" if SystemLanguage=="English" else "Статистика зображення", bg="#fff7d9", fg="#ffae00", font=("Arial", 40, "bold"), bd=0)
    TextFileText.place(y=25, relx=0.5, anchor='n')


    Widgets['BackButton'].place(x=60, y=24, relx=0, rely=0, anchor='nw')\

    Widgets['BackButton'].bind('<Enter>', BackButtonOnEnter)
    Widgets['BackButton'].bind('<Leave>', BackButtonOnLeave)
    Widgets['BackButton'].bind("<Button-1>", BackButtonOnClick)
    Widgets['BackButton'].bind("<ButtonRelease-1>", lambda Event:BackButtonRelease(Event, lambda:OpenShowResultFile(ContourButtonIndex)))



    
    CreatedImages=[ResultImage for ResultImage in os.listdir(ApplicationPath+'/Cash/ResultsFiles') if os.path.isdir(os.path.join(ApplicationPath+'/Cash/ResultsFiles', ResultImage))]
    CreatedImages = sorted(CreatedImages, key=lambda File: os.stat(ApplicationPath+'/Cash/ResultsFiles/'+File).st_birthtime, reverse=True)
    CreatedImage=CreatedImages[ContourButtonIndex]
    
    StatisticText=open(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage+'/ImageStatistic.txt', 'r').read()
    StatistiTextFile=Text(IBNGWindow, font="Arial 30 bold", bg="#fff9e9", borderwidth=0, highlightthickness=0, fg='#fdb84e')
    StatistiTextFile.tag_configure("centred", justify='center')
    StatistiTextFile.insert("end", StatisticText)
    StatistiTextFile.tag_add("centred", "1.0", "end")
    StatistiTextFile.configure(state='disabled') 
    StatistiTextFile.place(x=2, y=105, rely=0, relx=0, anchor='nw', height=int(IBNGWindow.winfo_height())-105, width=int(IBNGWindow.winfo_width())-4)

    

    Widgets['DownloadButton'].place(x=-60, y=18, relx=1, rely=0, anchor='ne')

    Widgets['DownloadButton'].bind('<Enter>', DownloadButtonOnEnter)
    Widgets['DownloadButton'].bind('<Leave>', DownloadButtonOnLeave)
    Widgets['DownloadButton'].bind("<Button-1>", DownloadButtonOnClick)
    Widgets['DownloadButton'].bind("<ButtonRelease-1>", lambda Event:DownloadButtonRelease(Event, CreatedImage, StatisticText, 'Statistic'))
    


    IBNGWindow.unbind("<Configure>")



    def OnWindowResize(Event):
        StatistiTextFile.place(x=2, y=99, rely=0, relx=0, anchor='nw', height=int(IBNGWindow.winfo_height())-101, width=int(IBNGWindow.winfo_width())-4)
        


    IBNGWindow.bind("<Configure>", OnWindowResize)


















def OpenShowResultFile(ContourButtonIndex):
    global Widgets
    global ResultFileName
    global IsEnterTextFileButton
    
    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
    [IBNGWindow.unbind_all(Event) for Event in Bindings]
    [IBNGWindow.unbind(Event) for Event in Bindings]
    for WindowElement in IBNGWindow.winfo_children():
       WindowElement.destroy()
    WidgetsInWindow=['BackgroundDetail3', 'PaletteResultFileIcon', 'ImageByNumberResultFileIcon', 'TextFileResultFileIcon', 'ImageByColorFromStockResultFileIcon', 'PaletteResultFileText', 'StockImageColorResultFileText', 'ImageByNumberResultFileText', 'ImageStatisticsResultFileText', 'BackButton', 'ProcessFilePlace2', 'PaletteCreateIcon']
    Widgets = {WidgetInformation[0]: Label(IBNGWindow, image=WidgetInformation[1], bg="#"+WidgetInformation[2], bd=0) for WidgetInformation in WidgetsInformation if WidgetInformation[0] in WidgetsInWindow}

    IBNGWindow.update()


    Widgets['BackgroundDetail3'].place(y=0, relx=0.5, anchor='n')


    
    CreatedImages=[ResultImage for ResultImage in os.listdir(ApplicationPath+'/Cash/ResultsFiles') if os.path.isdir(os.path.join(ApplicationPath+'/Cash/ResultsFiles', ResultImage))]
    CreatedImages = sorted(CreatedImages, key=lambda File: os.stat(ApplicationPath+'/Cash/ResultsFiles/'+File).st_birthtime, reverse=True)
    CreatedImage=CreatedImages[ContourButtonIndex]
    CreatedImageSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12).getbbox(CreatedImage)
    CreatedImageSize=CreatedImageSize[2]-CreatedImageSize[0]
    if CreatedImageSize<220/860*IBNGWindow.winfo_width():
        CreatedImageText=CreatedImage
    else:
        CreatedImageText=CreatedImage
        while CreatedImageSize>=220/860*IBNGWindow.winfo_width():
            CreatedImageSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12).getbbox(CreatedImageText+'...')
            CreatedImageSize=CreatedImageSize[2]-CreatedImageSize[0]
            CreatedImageText=CreatedImageText[:-1]
        CreatedImageText+='...'
    ResultFileName=Label(IBNGWindow, text=CreatedImageText, bg="#fff7d9", fg="#ffae00", font=("Arial", 40, "bold"), bd=0)
    ResultFileName.place(y=25, relx=0.5, anchor='n')


    Widgets['TextFileResultFileIcon'].place(x=-400, y=-120, relx=0.5, rely=0.5, anchor='center')
    if int(IBNGWindow.winfo_width())<1100:
        Widgets['TextFileResultFileIcon'].place(x=19, y=-120, relx=0, rely=0.5, anchor='w')
    Widgets['ImageStatisticsResultFileText'].place(x=-400, y=33, relx=0.5, rely=0.5, anchor='center')
    if int(IBNGWindow.winfo_width())<1100:
        Widgets['ImageStatisticsResultFileText'].place(x=63, y=33, relx=0, rely=0.5, anchor='w')
    IsEnterTextFileButton=False
    Widgets['TextFileResultFileIcon'].bind('<Enter>', TextFileButtonOnEnter)
    Widgets['TextFileResultFileIcon'].bind('<Leave>', TextFileButtonOnLeave)
    Widgets['TextFileResultFileIcon'].bind("<Button-1>", TextFileButtonOnClick)
    Widgets['TextFileResultFileIcon'].bind("<ButtonRelease-1>", lambda Event:TextFileButtonRelease(Event, ContourButtonIndex))



        
    Widgets['PaletteResultFileIcon'].place(x=0, y=-120, relx=0.5, rely=0.5, anchor='center')
    Widgets['PaletteResultFileText'].place(x=0, y=33, relx=0.5, rely=0.5, anchor='center')
    IsEnterPaletteButton=False
    Widgets['PaletteResultFileIcon'].bind('<Enter>', PaletteButtonOnEnter)
    Widgets['PaletteResultFileIcon'].bind('<Leave>', PaletteButtonOnLeave)
    Widgets['PaletteResultFileIcon'].bind("<Button-1>", PaletteButtonOnClick)
    Widgets['PaletteResultFileIcon'].bind("<ButtonRelease-1>", lambda Event:PaletteButtonRelease(Event, ContourButtonIndex))



    
    Widgets['ImageByColorFromStockResultFileIcon'].place(x=400, y=-120, relx=0.5, rely=0.5, anchor='center') 
    if int(IBNGWindow.winfo_width())<1100:
        Widgets['ImageByColorFromStockResultFileIcon'].place(x=-19, y=-120, relx=1, rely=0.5, anchor='e')
    Widgets['StockImageColorResultFileText'].place(x=400, y=33, relx=0.5, rely=0.5, anchor='center')
    if int(IBNGWindow.winfo_width())<1100:
        Widgets['StockImageColorResultFileText'].place(x=-50, y=33, relx=1, rely=0.5, anchor='e')
    IsEnterImageByColorFromStockButton=False
    Widgets['ImageByColorFromStockResultFileIcon'].bind('<Enter>', ImageByColorFromStockButtonOnEnter)
    Widgets['ImageByColorFromStockResultFileIcon'].bind('<Leave>', ImageByColorFromStockButtonOnLeave)
    Widgets['ImageByColorFromStockResultFileIcon'].bind("<Button-1>", ImageByColorFromStockButtonOnClick)
    Widgets['ImageByColorFromStockResultFileIcon'].bind("<ButtonRelease-1>", lambda Event:ImageByColorFromStockButtonRelease(Event, ContourButtonIndex))



        
    Widgets['ImageByNumberResultFileIcon'].place(x=0, y=190, relx=0.5, rely=0.5, anchor='center')
    Widgets['ImageByNumberResultFileText'].place(x=0, y=343, relx=0.5, rely=0.5, anchor='center')
    if 'ImageByNumberCreatedText' in Widgets and Widgets['ImageByNumberCreatedText'].place_info() != {} and int(IBNGWindow.winfo_width())<724 and Widgets['ImageByNumberCreatedText'].place_info()['anchor']=='center':
        Widgets['ImageByNumberResultFileText'].place(x=0, y=-6, relx=0.5, rely=1, anchor='s')
    IsEnterImageByNumberButton=False
    Widgets['ImageByNumberResultFileIcon'].bind('<Enter>', ImageByNumberButtonOnEnter)
    Widgets['ImageByNumberResultFileIcon'].bind('<Leave>', ImageByNumberButtonOnLeave)
    Widgets['ImageByNumberResultFileIcon'].bind("<Button-1>", ImageByNumberButtonOnClick)
    Widgets['ImageByNumberResultFileIcon'].bind("<ButtonRelease-1>", lambda Event:ImageByNumberButtonRelease(Event, ContourButtonIndex))




    Widgets['BackButton'].place(x=60, y=23, anchor='ne')

    IsEnterBackButton=False

    Widgets['BackButton'].bind('<Enter>', BackButtonOnEnter)
    Widgets['BackButton'].bind('<Leave>', BackButtonOnLeave)
    Widgets['BackButton'].bind("<Button-1>", BackButtonOnClick)
    Widgets['BackButton'].bind("<ButtonRelease-1>", lambda Event:BackButtonRelease(Event, OpenMainWindow))



    IBNGWindow.unbind("<Configure>")



   
    def OnWindowResize(Event):
        if 'ImageByNumberResultFileText' in Widgets and Widgets['ImageByNumberResultFileText'].place_info() != {} and int(IBNGWindow.winfo_height())<724 and Widgets['ImageByNumberResultFileText'].place_info()['anchor']=='center':
            Widgets['ImageByNumberResultFileText'].place(x=0, y=-6, relx=0.5, rely=1, anchor='s')
        elif 'ImageByNumberResultFileText' in Widgets and Widgets['ImageByNumberResultFileText'].place_info() != {} and int(IBNGWindow.winfo_height())>=724 and Widgets['ImageByNumberResultFileText'].place_info()['anchor']=='s':
            Widgets['ImageByNumberResultFileText'].place(x=0, y=343, relx=0.5, rely=0.5, anchor='center')
        if int(IBNGWindow.winfo_width())<1100:
            if 'TextFileResultFileIcon' in Widgets and Widgets['TextFileResultFileIcon'].place_info() != {} and Widgets['TextFileResultFileIcon'].place_info()['anchor']=='center':
                Widgets['TextFileResultFileIcon'].place(x=19, y=-120, relx=0, rely=0.5, anchor='w')
            if 'ImageByColorFromStockResultFileIcon' in Widgets and Widgets['ImageByColorFromStockResultFileIcon'].place_info() != {} and Widgets['ImageByColorFromStockResultFileIcon'].place_info()['anchor']=='center':
                Widgets['ImageByColorFromStockResultFileIcon'].place(x=-19, y=-120, relx=1, rely=0.5, anchor='e')
            if 'ImageStatisticsResultFileText' in Widgets and Widgets['ImageStatisticsResultFileText'].place_info() != {} and Widgets['ImageStatisticsResultFileText'].place_info()['anchor']=='center':
                Widgets['ImageStatisticsResultFileText'].place(x=63, y=33, relx=0, rely=0.5, anchor='w')
            if 'StockImageColorResultFileText' in Widgets and Widgets['StockImageColorResultFileText'].place_info() != {} and Widgets['StockImageColorResultFileText'].place_info()['anchor']=='center':
                Widgets['StockImageColorResultFileText'].place(x=-50, y=33, relx=1, rely=0.5, anchor='e')
        else:
            if 'TextFileResultFileIcon' in Widgets and Widgets['TextFileResultFileIcon'].place_info() != {} and Widgets['TextFileResultFileIcon'].place_info()['anchor']=='w':
                Widgets['TextFileResultFileIcon'].place(x=-400, y=-120, relx=0.5, rely=0.5, anchor='center')
            if 'ImageByColorFromStockResultFileIcon' in Widgets and Widgets['ImageByColorFromStockResultFileIcon'].place_info() != {} and Widgets['ImageByColorFromStockResultFileIcon'].place_info()['anchor']=='e':
                Widgets['ImageByColorFromStockResultFileIcon'].place(x=400, y=-120, relx=0.5, rely=0.5, anchor='center')
            if 'ImageStatisticsResultFileText' in Widgets and Widgets['ImageStatisticsResultFileText'].place_info() != {} and Widgets['ImageStatisticsResultFileText'].place_info()['anchor']=='w':
                Widgets['ImageStatisticsResultFileText'].place(x=-400, y=33, relx=0.5, rely=0.5, anchor='center')
            if 'StockImageColorResultFileText' in Widgets and Widgets['StockImageColorResultFileText'].place_info() != {} and Widgets['StockImageColorResultFileText'].place_info()['anchor']=='e':
                Widgets['StockImageColorResultFileText'].place(x=400, y=33, relx=0.5, rely=0.5, anchor='center')
        if ResultFileName.winfo_exists()==1:
            CreatedImageSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12).getbbox(CreatedImage)
            CreatedImageSize=CreatedImageSize[2]-CreatedImageSize[0]
            if CreatedImageSize<220/860*IBNGWindow.winfo_width():
                CreatedImageText=CreatedImage
            else:
                CreatedImageText=CreatedImage
                while CreatedImageSize>=220/860*IBNGWindow.winfo_width():
                    CreatedImageSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12).getbbox(CreatedImageText+'...')
                    CreatedImageSize=CreatedImageSize[2]-CreatedImageSize[0]
                    CreatedImageText=CreatedImageText[:-1]
                CreatedImageText+='...'
            CreatedImageSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 12).getbbox(CreatedImageText)
            CreatedImageSize=CreatedImageSize[2]-CreatedImageSize[0]
            ResultFileName['text']=CreatedImageText


    IBNGWindow.bind("<Configure>", OnWindowResize)
    IBNGWindow.minsize(860, 700)











def PaletteButtonOnClick(Event):
    def PaletteButtonEnterAnimate(Width, Height):
        if Width > 250:
            Width -= 2
            Height -= 2
            PaletteResultFileButton=Image.new('RGBA', (260, 260), color = (255, 255, 255, 0))
            PaletteResultFileButtonOld=PillowImages['PaletteResultFileIcon'].resize((Width, Height))
            PaletteResultFileButton.paste(PaletteResultFileButtonOld, ((260-Width)//2, (260-Height)//2), PaletteResultFileButtonOld)
            TkImages['PaletteResultFileIcon'] = ImageTk.PhotoImage(PaletteResultFileButton)
            Widgets['PaletteResultFileIcon']['image'] = TkImages['PaletteResultFileIcon']
            IBNGWindow.after(1, PaletteButtonEnterAnimate, Width, Height)
    PaletteButtonEnterAnimate(260, 260)

def PaletteButtonRelease(Event, ContourButtonIndex):
    def PaletteButtonEnterAnimate(Width, Height):
        global IsEnterPaletteButton
        if Width < 260:
            Width += 2
            Height += 2
            PaletteResultFileButton=Image.new('RGBA', (260, 260), color = (255, 255, 255, 0))
            PaletteResultFileButtonOld=PillowImages['PaletteResultFileIcon'].resize((Width, Height))
            PaletteResultFileButton.paste(PaletteResultFileButtonOld, ((260-Width)//2, (260-Height)//2), PaletteResultFileButtonOld)
            TkImages['PaletteResultFileIcon'] = ImageTk.PhotoImage(PaletteResultFileButton)
            Widgets['PaletteResultFileIcon']['image'] = TkImages['PaletteResultFileIcon']
            IBNGWindow.after(1, PaletteButtonEnterAnimate, Width, Height)
        else:
            if IsEnterPaletteButton == True:
                def GoToAnotherPage():
                    IsEnterPaletteButton=False
                    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
                    [IBNGWindow.unbind_all(Event) for Event in Bindings]
                    [IBNGWindow.unbind(Event) for Event in Bindings]
                    for WindowElement in IBNGWindow.winfo_children():
                       WindowElement.destroy()
                    OpenShowPaletteButton(ContourButtonIndex)
                IBNGWindow.after(10, GoToAnotherPage)
    PaletteButtonEnterAnimate(250, 250)
   


def PaletteButtonOnEnter(Event):
   global IsEnterPaletteButton
   IsEnterPaletteButton=True

   
def PaletteButtonOnLeave(Event):
   global IsEnterPaletteButton
   IsEnterPaletteButton=False







def OpenShowPaletteButton(ContourButtonIndex):
    global PaletteTkImage
    global Palette
    global Widgets
    global PaletteText
    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
    [IBNGWindow.unbind_all(Event) for Event in Bindings]
    [IBNGWindow.unbind(Event) for Event in Bindings]
    for WindowElement in IBNGWindow.winfo_children():
       WindowElement.destroy()
    WidgetsInWindow = ['BackgroundDetail3', 'BackButton', 'DownloadButton', 'ImageUploadedIcon']
    Widgets = {WidgetInformation[0]: Label(IBNGWindow, image=WidgetInformation[1], bg="#"+WidgetInformation[2], bd=0) for WidgetInformation in WidgetsInformation if WidgetInformation[0] in WidgetsInWindow}

    IBNGWindow.update()


    
    Widgets['BackgroundDetail3'].place(y=0, rely=0, relx=0.5, anchor='n')


    PaletteText=Label(IBNGWindow, text="Palette" if SystemLanguage=="English" else "Палітра", bg="#fff7d9", fg="#ffae00", font=("Arial", 40, "bold"), bd=0)
    PaletteText.place(y=25, relx=0.5, anchor='n')


    Widgets['BackButton'].place(x=60, y=24, relx=0, rely=0, anchor='nw')\

    Widgets['BackButton'].bind('<Enter>', BackButtonOnEnter)
    Widgets['BackButton'].bind('<Leave>', BackButtonOnLeave)
    Widgets['BackButton'].bind("<Button-1>", BackButtonOnClick)
    Widgets['BackButton'].bind("<ButtonRelease-1>", lambda Event:BackButtonRelease(Event, lambda:OpenShowResultFile(ContourButtonIndex)))



    
    CreatedImages=[ResultImage for ResultImage in os.listdir(ApplicationPath+'/Cash/ResultsFiles') if os.path.isdir(os.path.join(ApplicationPath+'/Cash/ResultsFiles', ResultImage))]
    CreatedImages = sorted(CreatedImages, key=lambda File: os.stat(ApplicationPath+'/Cash/ResultsFiles/'+File).st_birthtime, reverse=True)
    CreatedImage=CreatedImages[ContourButtonIndex]
    
    PaletteImage=Image.open(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage+'/PalettesForImageByNumber.png').convert("RGBA")
    WidthPaletteImage, HeightPaletteImage=PaletteImage.size
    if WidthPaletteImage/850 >= HeightPaletteImage/590:
        PaletteImageResize=PaletteImage.resize((850, int(850/WidthPaletteImage*HeightPaletteImage)))
    else:
        PaletteImageResize=PaletteImage.resize((int(590/HeightPaletteImage*WidthPaletteImage), 590))
    PaletteImageWidth, PaletteImageHeight=PaletteImageResize.size
    ShowPaletteImage=Image.new('RGBA', (PaletteImageWidth+10, PaletteImageHeight+10), color = (253, 202, 84,255))
    ShowPaletteImage.paste(PaletteImageResize, (5, 5), PaletteImageResize)
    PaletteTkImage=ImageTk.PhotoImage(ShowPaletteImage)
    Palette=Label(IBNGWindow, image=PaletteTkImage, bg="#fff9e9", bd=0)
    Palette.place(x=0, y=48, rely=0.5, relx=0.5, anchor='center')

    


    Widgets['DownloadButton'].place(x=-60, y=18, relx=1, rely=0, anchor='ne')

    Widgets['DownloadButton'].bind('<Enter>', DownloadButtonOnEnter)
    Widgets['DownloadButton'].bind('<Leave>', DownloadButtonOnLeave)
    Widgets['DownloadButton'].bind("<Button-1>", DownloadButtonOnClick)
    Widgets['DownloadButton'].bind("<ButtonRelease-1>", lambda Event:DownloadButtonRelease(Event, CreatedImage, PaletteImage, 'Palette'))
    


    IBNGWindow.unbind("<Configure>")




















def ImageByColorFromStockButtonOnClick(Event):
    def ImageByColorFromStockButtonEnterAnimate(Width, Height):
        if Width > 250:
            Width -= 2
            Height -= 2
            ImageByColorFromStockResultFileButton=Image.new('RGBA', (260, 260), color = (255, 255, 255, 0))
            ImageByColorFromStockResultFileButtonOld=PillowImages['ImageByColorFromStockResultFileIcon'].resize((Width, Height))
            ImageByColorFromStockResultFileButton.paste(ImageByColorFromStockResultFileButtonOld, ((260-Width)//2, (260-Height)//2), ImageByColorFromStockResultFileButtonOld)
            TkImages['ImageByColorFromStockResultFileIcon'] = ImageTk.PhotoImage(ImageByColorFromStockResultFileButton)
            Widgets['ImageByColorFromStockResultFileIcon']['image'] = TkImages['ImageByColorFromStockResultFileIcon']
            IBNGWindow.after(1, ImageByColorFromStockButtonEnterAnimate, Width, Height)
    ImageByColorFromStockButtonEnterAnimate(260, 260)

def ImageByColorFromStockButtonRelease(Event, ContourButtonIndex):
    def ImageByColorFromStockButtonEnterAnimate(Width, Height):
        global IsEnterImageByColorFromStockButton
        if Width < 260:
            Width += 2
            Height += 2
            ImageByColorFromStockResultFileButton=Image.new('RGBA', (260, 260), color = (255, 255, 255, 0))
            ImageByColorFromStockResultFileButtonOld=PillowImages['ImageByColorFromStockResultFileIcon'].resize((Width, Height))
            ImageByColorFromStockResultFileButton.paste(ImageByColorFromStockResultFileButtonOld, ((260-Width)//2, (260-Height)//2), ImageByColorFromStockResultFileButtonOld)
            TkImages['ImageByColorFromStockResultFileIcon'] = ImageTk.PhotoImage(ImageByColorFromStockResultFileButton)
            Widgets['ImageByColorFromStockResultFileIcon']['image'] = TkImages['ImageByColorFromStockResultFileIcon']
            IBNGWindow.after(1, ImageByColorFromStockButtonEnterAnimate, Width, Height)
        else:
            if IsEnterImageByColorFromStockButton == True:
                def GoToAnotherPage():
                    IsEnterImageByColorFromStockButton=False
                    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
                    [IBNGWindow.unbind_all(Event) for Event in Bindings]
                    [IBNGWindow.unbind(Event) for Event in Bindings]
                    for WindowElement in IBNGWindow.winfo_children():
                       WindowElement.destroy()
                    OpenShowImageByColorFromStockButton(ContourButtonIndex)
                IBNGWindow.after(100, GoToAnotherPage)
    ImageByColorFromStockButtonEnterAnimate(250, 250)
   


def ImageByColorFromStockButtonOnEnter(Event):
   global IsEnterImageByColorFromStockButton
   IsEnterImageByColorFromStockButton=True

   
def ImageByColorFromStockButtonOnLeave(Event):
   global IsEnterImageByColorFromStockButton
   IsEnterImageByColorFromStockButton=False



def OpenShowImageByColorFromStockButton(ContourButtonIndex):
    global ImageByColorFromStockTkImage
    global ImageByColorFromStock
    global Widgets
    global ImageByColorFromStockText
    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
    [IBNGWindow.unbind_all(Event) for Event in Bindings]
    [IBNGWindow.unbind(Event) for Event in Bindings]
    for WindowElement in IBNGWindow.winfo_children():
       WindowElement.destroy()
    WidgetsInWindow = ['BackgroundDetail3', 'BackButton', 'DownloadButton', 'ImageUploadedIcon']
    Widgets = {WidgetInformation[0]: Label(IBNGWindow, image=WidgetInformation[1], bg="#"+WidgetInformation[2], bd=0) for WidgetInformation in WidgetsInformation if WidgetInformation[0] in WidgetsInWindow}

    IBNGWindow.update()


    
    Widgets['BackgroundDetail3'].place(y=0, rely=0, relx=0.5, anchor='n')


    ImageByColorFromStockText=Label(IBNGWindow, text="Image By Color From Stock" if SystemLanguage=="English" else 'Зображення з кольорами зі складу', bg="#fff7d9", fg="#ffae00", font=("Arial", 40, "bold"), bd=0)
    ImageByColorFromStockText.place(y=25, relx=0.5, anchor='n')


    Widgets['BackButton'].place(x=60, y=24, relx=0, rely=0, anchor='nw')\

    Widgets['BackButton'].bind('<Enter>', BackButtonOnEnter)
    Widgets['BackButton'].bind('<Leave>', BackButtonOnLeave)
    Widgets['BackButton'].bind("<Button-1>", BackButtonOnClick)
    Widgets['BackButton'].bind("<ButtonRelease-1>", lambda Event:BackButtonRelease(Event, lambda:OpenShowResultFile(ContourButtonIndex)))



    
    CreatedImages=[ResultImage for ResultImage in os.listdir(ApplicationPath+'/Cash/ResultsFiles') if os.path.isdir(os.path.join(ApplicationPath+'/Cash/ResultsFiles', ResultImage))]
    CreatedImages = sorted(CreatedImages, key=lambda File: os.stat(ApplicationPath+'/Cash/ResultsFiles/'+File).st_birthtime, reverse=True)
    CreatedImage=CreatedImages[ContourButtonIndex]
    
    ImageByColorFromStockImage=Image.open(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage+'/StockImageColor.png').convert("RGBA")
    WidthImageByColorFromStockImage, HeightImageByColorFromStockImage=ImageByColorFromStockImage.size
    if WidthImageByColorFromStockImage/850 >= HeightImageByColorFromStockImage/590:
        ImageByColorFromStockImageResize=ImageByColorFromStockImage.resize((850, int(850/WidthImageByColorFromStockImage*HeightImageByColorFromStockImage)))
    else:
        ImageByColorFromStockImageResize=ImageByColorFromStockImage.resize((int(590/HeightImageByColorFromStockImage*WidthImageByColorFromStockImage), 590))
    ImageByColorFromStockTkImage=ImageTk.PhotoImage(ImageByColorFromStockImageResize)
    ImageByColorFromStock=Label(IBNGWindow, image=ImageByColorFromStockTkImage, bg="#fff9e9", bd=0)
    ImageByColorFromStock.place(x=0, y=48, rely=0.5, relx=0.5, anchor='center')

    


    Widgets['DownloadButton'].place(x=-60, y=18, relx=1, rely=0, anchor='ne')

    Widgets['DownloadButton'].bind('<Enter>', DownloadButtonOnEnter)
    Widgets['DownloadButton'].bind('<Leave>', DownloadButtonOnLeave)
    Widgets['DownloadButton'].bind("<Button-1>", DownloadButtonOnClick)
    Widgets['DownloadButton'].bind("<ButtonRelease-1>", lambda Event:DownloadButtonRelease(Event, CreatedImage, ImageByColorFromStockImage, 'ImageByColorFromStock'))
    


    IBNGWindow.unbind("<Configure>")














def ImageByNumberButtonOnClick(Event):
    def ImageByNumberButtonEnterAnimate(Width, Height):
        if Width > 250:
            Width -= 2
            Height -= 2
            ImageByNumberResultFileButton=Image.new('RGBA', (260, 260), color = (255, 255, 255, 0))
            ImageByNumberResultFileButtonOld=PillowImages['ImageByNumberResultFileIcon'].resize((Width, Height))
            ImageByNumberResultFileButton.paste(ImageByNumberResultFileButtonOld, ((260-Width)//2, (260-Height)//2), ImageByNumberResultFileButtonOld)
            TkImages['ImageByNumberResultFileIcon'] = ImageTk.PhotoImage(ImageByNumberResultFileButton)
            Widgets['ImageByNumberResultFileIcon']['image'] = TkImages['ImageByNumberResultFileIcon']
            IBNGWindow.after(1, ImageByNumberButtonEnterAnimate, Width, Height)
    ImageByNumberButtonEnterAnimate(260, 260)

def ImageByNumberButtonRelease(Event, ContourButtonIndex):
    def ImageByNumberButtonEnterAnimate(Width, Height):
        global IsEnterImageByNumberButton
        if Width < 260:
            Width += 2
            Height += 2
            ImageByNumberResultFileButton=Image.new('RGBA', (260, 260), color = (255, 255, 255, 0))
            ImageByNumberResultFileButtonOld=PillowImages['ImageByNumberResultFileIcon'].resize((Width, Height))
            ImageByNumberResultFileButton.paste(ImageByNumberResultFileButtonOld, ((260-Width)//2, (260-Height)//2), ImageByNumberResultFileButtonOld)
            TkImages['ImageByNumberResultFileIcon'] = ImageTk.PhotoImage(ImageByNumberResultFileButton)
            Widgets['ImageByNumberResultFileIcon']['image'] = TkImages['ImageByNumberResultFileIcon']
            IBNGWindow.after(1, ImageByNumberButtonEnterAnimate, Width, Height)
        else:
            if IsEnterImageByNumberButton == True:
                def GoToAnotherPage():
                    IsEnterImageByNumberButton=False
                    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
                    [IBNGWindow.unbind_all(Event) for Event in Bindings]
                    [IBNGWindow.unbind(Event) for Event in Bindings]
                    for WindowElement in IBNGWindow.winfo_children():
                       WindowElement.destroy()
                    OpenShowImageByNumberButton(ContourButtonIndex)
                IBNGWindow.after(100, GoToAnotherPage)
    ImageByNumberButtonEnterAnimate(250, 250)
   


def ImageByNumberButtonOnEnter(Event):
   global IsEnterImageByNumberButton
   IsEnterImageByNumberButton=True

   
def ImageByNumberButtonOnLeave(Event):
   global IsEnterImageByNumberButton
   IsEnterImageByNumberButton=False








def OpenShowImageByNumberButton(ContourButtonIndex):
    global ImageByNumberTkImage
    global ImageByNumber
    global Widgets
    global ImageByNumberText
    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
    [IBNGWindow.unbind_all(Event) for Event in Bindings]
    [IBNGWindow.unbind(Event) for Event in Bindings]
    for WindowElement in IBNGWindow.winfo_children():
       WindowElement.destroy()
    WidgetsInWindow = ['BackgroundDetail3', 'BackButton', 'DownloadButton', 'ImageUploadedIcon']
    Widgets = {WidgetInformation[0]: Label(IBNGWindow, image=WidgetInformation[1], bg="#"+WidgetInformation[2], bd=0) for WidgetInformation in WidgetsInformation if WidgetInformation[0] in WidgetsInWindow}

    IBNGWindow.update()


    
    Widgets['BackgroundDetail3'].place(y=0, rely=0, relx=0.5, anchor='n')


    ImageByNumberText=Label(IBNGWindow, text="Image By Number" if SystemLanguage=="English" else 'Зображення по номерам', bg="#fff7d9", fg="#ffae00", font=("Arial", 40, "bold"), bd=0)
    ImageByNumberText.place(y=25, relx=0.5, anchor='n')


    Widgets['BackButton'].place(x=60, y=24, relx=0, rely=0, anchor='nw')\

    Widgets['BackButton'].bind('<Enter>', BackButtonOnEnter)
    Widgets['BackButton'].bind('<Leave>', BackButtonOnLeave)
    Widgets['BackButton'].bind("<Button-1>", BackButtonOnClick)
    Widgets['BackButton'].bind("<ButtonRelease-1>", lambda Event:BackButtonRelease(Event, lambda:OpenShowResultFile(ContourButtonIndex)))



    
    CreatedImages=[ResultImage for ResultImage in os.listdir(ApplicationPath+'/Cash/ResultsFiles') if os.path.isdir(os.path.join(ApplicationPath+'/Cash/ResultsFiles', ResultImage))]
    CreatedImages = sorted(CreatedImages, key=lambda File: os.stat(ApplicationPath+'/Cash/ResultsFiles/'+File).st_birthtime, reverse=True)
    CreatedImage=CreatedImages[ContourButtonIndex]
    
    ImageByNumberImage=Image.open(ApplicationPath+'/Cash/ResultsFiles/'+CreatedImage+'/ImageByNumber.png').convert("RGBA")
    WidthImageByNumberImage, HeightImageByNumberImage=ImageByNumberImage.size
    if WidthImageByNumberImage/850 >= HeightImageByNumberImage/590:
        ImageByNumberImageResize=ImageByNumberImage.resize((850, int(850/WidthImageByNumberImage*HeightImageByNumberImage)))
    else:
        ImageByNumberImageResize=ImageByNumberImage.resize((int(590/HeightImageByNumberImage*WidthImageByNumberImage), 590))
    ImageByNumberTkImage=ImageTk.PhotoImage(ImageByNumberImageResize)
    ImageByNumber=Label(IBNGWindow, image=ImageByNumberTkImage, bg="#fff9e9", bd=0)
    ImageByNumber.place(x=0, y=48, rely=0.5, relx=0.5, anchor='center')

    


    Widgets['DownloadButton'].place(x=-60, y=18, relx=1, rely=0, anchor='ne')

    Widgets['DownloadButton'].bind('<Enter>', DownloadButtonOnEnter)
    Widgets['DownloadButton'].bind('<Leave>', DownloadButtonOnLeave)
    Widgets['DownloadButton'].bind("<Button-1>", DownloadButtonOnClick)
    Widgets['DownloadButton'].bind("<ButtonRelease-1>", lambda Event:DownloadButtonRelease(Event, CreatedImage, ImageByNumberImage, 'ImageByNumber'))
    


    IBNGWindow.unbind("<Configure>")





def ImageUploadedAnimation(EntryAnimation):
    if 'ImageUploadedIcon' in Widgets:
        ImageUploadedIconY=int(Widgets['ImageUploadedIcon'].place_info()['y'])
        if ImageUploadedIconY<20 and EntryAnimation==True:
            Widgets['ImageUploadedIcon'].place(y=ImageUploadedIconY+8, rely=0, relx=0.5, anchor='n')
            IBNGWindow.after(10, lambda:ImageUploadedAnimation(True))
        elif ImageUploadedIconY>=20 and EntryAnimation==True:
            IBNGWindow.after(2000, lambda:ImageUploadedAnimation(False))
        elif ImageUploadedIconY>=-66 and EntryAnimation==False:
            Widgets['ImageUploadedIcon'].place(y=ImageUploadedIconY-10, rely=0, relx=0.5, anchor='n')
            IBNGWindow.after(7, lambda:ImageUploadedAnimation(False))
        else:
            Widgets['ImageUploadedIcon'].place_forget()



def StatisticUploadedAnimation(EntryAnimation):
    if 'StatisticUploadedIcon' in Widgets:
        StatisticUploadedIconY=int(Widgets['StatisticUploadedIcon'].place_info()['y'])
        if StatisticUploadedIconY<20 and EntryAnimation==True:
            Widgets['StatisticUploadedIcon'].place(y=StatisticUploadedIconY+8, rely=0, relx=0.5, anchor='n')
            IBNGWindow.after(10, lambda:StatisticUploadedAnimation(True))
        elif StatisticUploadedIconY>=20 and EntryAnimation==True:
            IBNGWindow.after(2000, lambda:StatisticUploadedAnimation(False))
        elif StatisticUploadedIconY>=-66 and EntryAnimation==False:
            Widgets['StatisticUploadedIcon'].place(y=StatisticUploadedIconY-10, rely=0, relx=0.5, anchor='n')
            IBNGWindow.after(7, lambda:StatisticUploadedAnimation(False))
        else:
            Widgets['StatisticUploadedIcon'].place_forget()


            

def DownloadButtonOnClick(Event):
    Widgets['DownloadButton']['image'] = TkImages['DownloadButtonClamped']


def DownloadButtonRelease(Event, ContourFolder, ImageToSave, FileType):
    Widgets['DownloadButton']['image'] = TkImages['DownloadButtonRealesed']
    if IsEnterDownloadButton == True:
        def GoToAnotherPage():
            if FileType != 'Statistic':
                PathToSaveFile=filedialog.asksaveasfilename(initialfile=ContourFolder+FileType, defaultextension=DownloadFileFormat, confirmoverwrite = False, filetypes = [(DownloadFileFormat[1:].upper(), '*'+DownloadFileFormat)])
                if PathToSaveFile != "":
                    Widgets['ImageUploadedIcon'].place(y=-66, rely=0, relx=0.5, anchor='n')
                    Widgets['ImageUploadedIcon'].lift()
                    IBNGWindow.after(5, lambda:ImageUploadedAnimation(True))
                    ImageToSave.save(PathToSaveFile)
            else:
                PathToSaveFile=filedialog.asksaveasfilename(initialfile=ContourFolder+FileType, defaultextension=".txt", confirmoverwrite = False, filetypes = [('TXT', '*.txt')])
                if PathToSaveFile != "":
                    Widgets['StatisticUploadedIcon'].place(y=-66, rely=0, relx=0.5, anchor='n')
                    Widgets['StatisticUploadedIcon'].lift()
                    IBNGWindow.after(5, lambda:StatisticUploadedAnimation(True))
                    open(PathToSaveFile, 'w').write(ImageToSave)

        IBNGWindow.after(100, GoToAnotherPage)
        


def DownloadButtonOnEnter(Event):
   global IsEnterDownloadButton
   IsEnterDownloadButton=True

def DownloadButtonOnLeave(Event):
   global IsEnterDownloadButton
   IsEnterDownloadButton=False
   




















































































































































































#Settings Button Animation

def SettingsButtonOnClick(Event):
    TkImages['SettingsButtonClamped'] = ImageTk.PhotoImage(PillowImages['SettingsButtonClamped'])
    Widgets['SettingsButton']['image'] = TkImages['SettingsButtonClamped']


def SettingsButtonRelease(Event):
    TkImages['SettingsButtonRealesed'] = ImageTk.PhotoImage(PillowImages['SettingsButtonRealesed'])
    Widgets['SettingsButton']['image'] = TkImages['SettingsButtonRealesed']
    if IsEnterSettingsButton == True:
        def GoToAnotherPage():
            [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
            [IBNGWindow.unbind_all(Event) for Event in Bindings]
            [IBNGWindow.unbind(Event) for Event in Bindings]
            for WindowElement in IBNGWindow.winfo_children():
                WindowElement.destroy()
            OpenSettingsWindow()
        IBNGWindow.after(100, GoToAnotherPage)
   


def SettingsButtonOnEnter(Event):
   global IsEnterSettingsButton
   IsEnterSettingsButton=True

def SettingsButtonOnLeave(Event):
   global IsEnterSettingsButton
   IsEnterSettingsButton=False
























def LanguageSettingsOnClick(Event):
    PriorityLanguageSettingsPlaceButtonClamped=PillowImages['PriorityLanguageSettingsPlaceButtonClamped'].copy()
    PriorityLanguageSettingsPlaceButtonClampedDraw=ImageDraw.Draw(PriorityLanguageSettingsPlaceButtonClamped)
    PriorityLanguageSettingsPlaceButtonClampedDraw.text((SystemLanguageWidth, SystemLanguageHeight), SystemLanguage, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28), fill=(255, 198, 72, 255))
    TkImages['PriorityLanguageSettingsPlaceButtonClamped']=ImageTk.PhotoImage(PriorityLanguageSettingsPlaceButtonClamped)
    Widgets['PriorityLanguageSettingsPlaceButton']['image'] = TkImages['PriorityLanguageSettingsPlaceButtonClamped']


def LanguageSettingsRelease(Event):
    PriorityLanguageSettingsPlaceButtonRealesed=PillowImages['PriorityLanguageSettingsPlaceButtonRealesed'].copy()
    PriorityLanguageSettingsPlaceButtonRealesedDraw=ImageDraw.Draw(PriorityLanguageSettingsPlaceButtonRealesed)
    PriorityLanguageSettingsPlaceButtonRealesedDraw.text((SystemLanguageWidth, SystemLanguageHeight), SystemLanguage, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28), fill=(255, 198, 72, 255))
    TkImages['PriorityLanguageSettingsPlaceButtonRealesed']=ImageTk.PhotoImage(PriorityLanguageSettingsPlaceButtonRealesed)
    Widgets['PriorityLanguageSettingsPlaceButton']['image'] = TkImages['PriorityLanguageSettingsPlaceButtonRealesed']
    if IsEnterLanguageSettings == True:
        def GoToAnotherPage():
            OpenChangeLanguageWindow()

        IBNGWindow.after(100, GoToAnotherPage)
        


def LanguageSettingsOnEnter(Event):
   global IsEnterLanguageSettings
   IsEnterLanguageSettings=True

def LanguageSettingsOnLeave(Event):
   global IsEnterLanguageSettings
   IsEnterLanguageSettings=False
   










def LanguageSettingsPlaceButtonOnClick(Event):
    if Event.y in [AllowY for AllowY in range(0, 62)] and Event.x in [AllowX for AllowX in range(0, 480)]:
        LanguageSettingsPlaceButtonEnglishClamped=PillowImages['LanguageSettingsPlaceButtonEnglishClamped'].copy()
        if SystemLanguage=="English":
            LanguageSettingsPlaceButtonEnglishClamped.paste(PillowImages['SettingsCheckMark'], (434, 19), mask=PillowImages['SettingsCheckMark'])
        elif SystemLanguage=="Ukrainian":
            LanguageSettingsPlaceButtonEnglishClamped.paste(PillowImages['SettingsCheckMark'], (434, 83), mask=PillowImages['SettingsCheckMark'])

        TkImages['LanguageSettingsPlaceButtonEnglishClamped']=ImageTk.PhotoImage(LanguageSettingsPlaceButtonEnglishClamped)
        Widgets['LanguageSettingsPlaceButton']['image'] = TkImages['LanguageSettingsPlaceButtonEnglishClamped']
    elif Event.y in [AllowY for AllowY in range(65, 127)] and Event.x in [AllowX for AllowX in range(0, 480)]:
        LanguageSettingsPlaceButtonUkrainianClamped=PillowImages['LanguageSettingsPlaceButtonUkrainianClamped'].copy()
        if SystemLanguage=="English":
            LanguageSettingsPlaceButtonUkrainianClamped.paste(PillowImages['SettingsCheckMark'], (434, 19), mask=PillowImages['SettingsCheckMark'])
        elif SystemLanguage=="Ukrainian":
            LanguageSettingsPlaceButtonUkrainianClamped.paste(PillowImages['SettingsCheckMark'], (434, 83), mask=PillowImages['SettingsCheckMark'])

        TkImages['LanguageSettingsPlaceButtonUkrainianClamped']=ImageTk.PhotoImage(LanguageSettingsPlaceButtonUkrainianClamped)
        Widgets['LanguageSettingsPlaceButton']['image'] = TkImages['LanguageSettingsPlaceButtonUkrainianClamped']







def LanguageSettingsPlaceButtonRealese(Event):
    global SystemLanguage
    global PillowImages
    global TkImages
    global WidgetsInformation
    global Widgets
    if Event.y in [AllowY for AllowY in range(0, 62)] and Event.x in [AllowX for AllowX in range(0, 480)] and SystemLanguage!="English":
        SystemLanguage="English"
        open(ApplicationPath+'/Cash/SystemLanguage.txt', 'w').write('English')
    elif Event.y in [AllowY for AllowY in range(65, 127)] and Event.x in [AllowX for AllowX in range(0, 480)] and SystemLanguage!="Ukrainian":
        SystemLanguage="Ukrainian"
        open(ApplicationPath+'/Cash/SystemLanguage.txt', 'w').write('Ukrainian')
        
    LanguageSettingsPlaceButtonRealesed=PillowImages['LanguageSettingsPlaceButtonRealesed'].copy()
    if SystemLanguage=="English":
        LanguageSettingsPlaceButtonRealesed.paste(PillowImages['SettingsCheckMark'], (434, 19), mask=PillowImages['SettingsCheckMark'])
    elif SystemLanguage=="Ukrainian":
        LanguageSettingsPlaceButtonRealesed.paste(PillowImages['SettingsCheckMark'], (434, 83), mask=PillowImages['SettingsCheckMark'])

    TkImages['LanguageSettingsPlaceButtonRealesed']=ImageTk.PhotoImage(LanguageSettingsPlaceButtonRealesed)
    Widgets['LanguageSettingsPlaceButton']['image'] = TkImages['LanguageSettingsPlaceButtonRealesed']

    if SystemLanguage=="English":
        PillowImages=PillowImagesEnglish
        TkImages=TkImagesEnglish
        WidgetsInformation=WidgetsInformationEnglish
        Widgets=WidgetsEnglish
    elif SystemLanguage=="Ukrainian":
        PillowImages=PillowImagesUkrainian
        TkImages=TkImagesUkrainian
        WidgetsInformation=WidgetsInformationUkrainian
        Widgets=WidgetsUkrainian

    OpenChangeLanguageWindow()
    
        


def OpenChangeLanguageWindow():
    global Widgets
    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
    [IBNGWindow.unbind_all(Event) for Event in Bindings]
    [IBNGWindow.unbind(Event) for Event in Bindings]
    for WindowElement in IBNGWindow.winfo_children():
       WindowElement.destroy()
    WidgetsInWindow=['BackgroundDetail3', 'LanguageText', 'LanguageSettingsPlaceButton', 'BackButton']
    Widgets = {WidgetInformation[0]: Label(IBNGWindow, image=WidgetInformation[1], bg="#"+WidgetInformation[2], bd=0) for WidgetInformation in WidgetsInformation if WidgetInformation[0] in WidgetsInWindow}

    IBNGWindow.update()
    

    Widgets['BackgroundDetail3'].place(y=-10, rely=0, relx=0.5, anchor='n')


    Widgets['LanguageText'].place(y=19, relx=0.5, anchor='n')

    
    LanguageSettingsPlaceButtonRealesed=PillowImages['LanguageSettingsPlaceButtonRealesed'].copy()
    if SystemLanguage=="English":
        LanguageSettingsPlaceButtonRealesed.paste(PillowImages['SettingsCheckMark'], (434, 19), mask=PillowImages['SettingsCheckMark'])
    elif SystemLanguage=="Ukrainian":
        LanguageSettingsPlaceButtonRealesed.paste(PillowImages['SettingsCheckMark'], (434, 83), mask=PillowImages['SettingsCheckMark'])

    TkImages['LanguageSettingsPlaceButtonRealesed']=ImageTk.PhotoImage(LanguageSettingsPlaceButtonRealesed)
    Widgets['LanguageSettingsPlaceButton']['image'] = TkImages['LanguageSettingsPlaceButtonRealesed']
        
    Widgets['LanguageSettingsPlaceButton'].place(x=0, y=152, relx=0.5, rely=0, anchor='n')
    Widgets['LanguageSettingsPlaceButton'].bind('<Button-1>', LanguageSettingsPlaceButtonOnClick)
    Widgets['LanguageSettingsPlaceButton'].bind('<ButtonRelease-1>', LanguageSettingsPlaceButtonRealese)

    


    Widgets['BackButton'].place(x=60, y=18, relx=0, rely=0, anchor='nw')

    Widgets['BackButton'].bind('<Enter>', BackButtonOnEnter)
    Widgets['BackButton'].bind('<Leave>', BackButtonOnLeave)
    Widgets['BackButton'].bind("<Button-1>", BackButtonOnClick)
    Widgets['BackButton'].bind("<ButtonRelease-1>", lambda Event:BackButtonRelease(Event, OpenSettingsWindow))
    









def ColorSetsSettingsOnClick(Event):
    ColorSetsSettingsPlaceButtonClamped=PillowImages['ColorSetsSettingsPlaceButtonClamped'].copy()
    ColorSetsSettingsPlaceButtonClampedDraw=ImageDraw.Draw(ColorSetsSettingsPlaceButtonClamped)
    StockColorsSetNameSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28).getbbox(StockColorsSetName)
    StockColorsSetNameWidth, StockColorsSetNameHeight=StockColorsSetNameSize[2]-StockColorsSetNameSize[0], StockColorsSetNameSize[3]+StockColorsSetNameSize[1]
      
    if StockColorsSetNameWidth<236:
        StockColorsSetNameText=StockColorsSetName
        StockColorsSetNameWidth, StockColorsSetNameHeight=422-StockColorsSetNameWidth, math.ceil((61-StockColorsSetNameHeight)/2)
    else:
        StockColorsSetNameText=StockColorsSetName
        while StockColorsSetNameWidth>=236:
            StockColorsSetNameSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28).getbbox(StockColorsSetNameText+'...')
            StockColorsSetNameWidth, StockColorsSetNameHeight=StockColorsSetNameSize[2]-StockColorsSetNameSize[0], StockColorsSetNameSize[3]+StockColorsSetNameSize[1]
            StockColorsSetNameText=StockColorsSetNameText[:-1]
        StockColorsSetNameText+='...'
        StockColorsSetNameWidth, StockColorsSetNameHeight=440-StockColorsSetNameWidth, math.ceil((61-StockColorsSetNameHeight)/2)
    
    ColorSetsSettingsPlaceButtonClampedDraw.text((StockColorsSetNameWidth, StockColorsSetNameHeight), StockColorsSetNameText, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28), fill=(255, 198, 72, 255))
    TkImages['ColorSetsSettingsPlaceButtonClamped']=ImageTk.PhotoImage(ColorSetsSettingsPlaceButtonClamped)
    Widgets['ColorSetsSettingsPlaceButton']['image'] = TkImages['ColorSetsSettingsPlaceButtonClamped']


def ColorSetsSettingsRelease(Event):
    ColorSetsSettingsPlaceButtonRealesed=PillowImages['ColorSetsSettingsPlaceButtonRealesed'].copy()
    ColorSetsSettingsPlaceButtonRealesedDraw=ImageDraw.Draw(ColorSetsSettingsPlaceButtonRealesed)
    StockColorsSetNameSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28).getbbox(StockColorsSetName)
    StockColorsSetNameWidth, StockColorsSetNameHeight=StockColorsSetNameSize[2]-StockColorsSetNameSize[0], StockColorsSetNameSize[3]+StockColorsSetNameSize[1]
      
    if StockColorsSetNameWidth<236:
        StockColorsSetNameText=StockColorsSetName
        StockColorsSetNameWidth, StockColorsSetNameHeight=422-StockColorsSetNameWidth, math.ceil((61-StockColorsSetNameHeight)/2)
    else:
        StockColorsSetNameText=StockColorsSetName
        while StockColorsSetNameWidth>=236:
            StockColorsSetNameSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28).getbbox(StockColorsSetNameText+'...')
            StockColorsSetNameWidth, StockColorsSetNameHeight=StockColorsSetNameSize[2]-StockColorsSetNameSize[0], StockColorsSetNameSize[3]+StockColorsSetNameSize[1]
            StockColorsSetNameText=StockColorsSetNameText[:-1]
        StockColorsSetNameText+='...'
        StockColorsSetNameWidth, StockColorsSetNameHeight=440-StockColorsSetNameWidth, math.ceil((61-StockColorsSetNameHeight)/2)
    
    ColorSetsSettingsPlaceButtonRealesedDraw.text((StockColorsSetNameWidth, StockColorsSetNameHeight), StockColorsSetNameText, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28), fill=(255, 198, 72, 255))
    TkImages['ColorSetsSettingsPlaceButtonRealesed']=ImageTk.PhotoImage(ColorSetsSettingsPlaceButtonRealesed)
    Widgets['ColorSetsSettingsPlaceButton']['image'] = TkImages['ColorSetsSettingsPlaceButtonRealesed']
    if IsEnterColorSetsSettings == True:
        def GoToAnotherPage():
            OpenChangeColorSetsWindow()

        IBNGWindow.after(100, GoToAnotherPage)
        


def ColorSetsSettingsOnEnter(Event):
   global IsEnterColorSetsSettings
   IsEnterColorSetsSettings=True

def ColorSetsSettingsOnLeave(Event):
   global IsEnterColorSetsSettings
   IsEnterColorSetsSettings=False
   









def ColorsSetSettingsOnClick(Event, ColorSetIndex):
    if StockColorsSetsUsedIndex == ColorSetIndex:
        Event.widget['image'] = StockColorsSetsUsedClampedImageTk[ColorSetIndex]
    else:
        Event.widget['image'] = StockColorsSetsClampedImageTk[ColorSetIndex]


def ColorsSetSettingsRelease(Event, ColorSetIndex):
    if StockColorsSetsUsedIndex == ColorSetIndex:
        Event.widget['image'] = StockColorsSetsUsedImageTk[ColorSetIndex]
    else:
        Event.widget['image'] = StockColorsSetsRealesedImageTk[ColorSetIndex]
    if IsEnterStockColorSets[ColorSetIndex] == True:
        def GoToAnotherPage():
            global AddColorsSetRgb
            global ColorSetName
            global ColorSetMode
            global ColorSetNameForEdit
            
            StockColorsSets=str(open(ApplicationPath+'/Cash/StockColorsSets.txt', 'r').read()).split('\n')
            if StockColorsSets[ColorSetIndex][:StockColorsSets[ColorSetIndex].find(':')]==StockColorsSetName:
                ColorSetMode=2
            else:
                ColorSetMode=1
            AddColorsSetRgb=ast.literal_eval(StockColorsSets[ColorSetIndex][StockColorsSets[ColorSetIndex].find(':')+1:])
            ColorSetName=StockColorsSets[ColorSetIndex][:StockColorsSets[ColorSetIndex].find(':')]
            ColorSetNameForEdit=ColorSetIndex
            OpenAddColorsSetSettingsWindow()  

        IBNGWindow.after(100, GoToAnotherPage)
        


def ColorsSetSettingsOnEnter(Event, ColorSetIndex):
   global IsEnterStockColorSets
   IsEnterStockColorSets[ColorSetIndex]=True

def ColorsSetSettingsOnLeave(Event, ColorSetIndex):
   global IsEnterStockColorSets
   IsEnterStockColorSets[ColorSetIndex]=False
   









def AddColorsSetSettingsOnClick(Event):
    AddColorSetSettingsPlaceButton['image'] = TkImages['AddColorSetSettingsPlaceButtonClamped']


def AddColorsSetSettingsRelease(Event):
    AddColorSetSettingsPlaceButton['image'] = TkImages['AddColorSetSettingsPlaceButtonRealesed']
    if IsEnterAddColorsSet == True:
        def GoToAnotherPage():
            global AddColorsSetRgb
            global ColorSetName
            global ColorSetMode
            ColorSetMode=0
            AddColorsSetRgb=[]
            ColorSetName="Color set "+str(len(StockColorsSets.split('\n'))+1)
            OpenAddColorsSetSettingsWindow()   

        IBNGWindow.after(100, GoToAnotherPage)
        


def AddColorsSetSettingsOnEnter(Event):
   global IsEnterAddColorsSet
   IsEnterAddColorsSet=True

def AddColorsSetSettingsOnLeave(Event):
   global IsEnterAddColorsSet
   IsEnterAddColorsSet=False













def AddColorsSetWidgetOnClick(Event, IndexAddColorsSet):
    if Event.y in [AllowY for AllowY in range(55, 81)] and Event.x in [AllowX for AllowX in range(55, 81)]:
        Event.widget['image'] = PaletteAddColorDeleteButtonClamped[IndexAddColorsSet]
    elif Event.y in [AllowY for AllowY in range(0, 81)] and Event.x in [AllowX for AllowX in range(0, 81)]:
        Event.widget['image'] = PaletteAddColorClamped[IndexAddColorsSet]







def AddColorsSetWidgetRelease(Event, IndexAddColorsSet):
    global AddColorsSetRgb
    if Event.y in [AllowY for AllowY in range(55, 81)] and Event.x in [AllowX for AllowX in range(55, 81)]:
        AddColorsSetRgb=AddColorsSetRgb[:IndexAddColorsSet]+AddColorsSetRgb[IndexAddColorsSet+1:]
        [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
        [IBNGWindow.unbind_all(Event) for Event in Bindings]
        [IBNGWindow.unbind(Event) for Event in Bindings]
        for WindowElement in IBNGWindow.winfo_children():
           WindowElement.destroy()
        OpenAddColorsSetSettingsWindow()
    elif Event.y in [AllowY for AllowY in range(0, 81)] and Event.x in [AllowX for AllowX in range(0, 81)]:
        ChoosenColor=colorchooser.askcolor(AddColorsSetRgb[IndexAddColorsSet], title="Edit Color" if SystemLanguage=="English" else "Редагувати колір")
        if ChoosenColor != (None, None) and ChoosenColor[0] not in AddColorsSetRgb:
            AddColorsSetRgb[IndexAddColorsSet]=ChoosenColor[0]
            Event.widget['image'] = PaletteAddColorDeleteButtonRealesed[IndexAddColorsSet]
            OpenAddColorsSetSettingsWindow()
        elif ChoosenColor[0] in AddColorsSetRgb and ChoosenColor[0] != AddColorsSetRgb[IndexAddColorsSet]:
            AddColorsSetRgb=AddColorsSetRgb[:IndexAddColorsSet]+AddColorsSetRgb[IndexAddColorsSet+1:]
            Event.widget['image'] = PaletteAddColorDeleteButtonRealesed[IndexAddColorsSet]
            OpenAddColorsSetSettingsWindow()
        else:
            Event.widget['image'] = PaletteAddColorDeleteButtonRealesed[IndexAddColorsSet]
    else:
        Event.widget['image'] = PaletteAddColorDeleteButtonRealesed[IndexAddColorsSet]









def AddColorPaletteButtonOnClick(Event):
    AddColorPaletteButton['image'] = TkImages['AddColorPaletteClamped']


def AddColorPaletteButtonRelease(Event):
    AddColorPaletteButton['image'] = TkImages['AddColorPaletteRealesed']
    if IsEnterAddColorPaletteButton == True:
        def GoToAnotherPage():
            global AddColorsSetRgb
            ChoosenColor=colorchooser.askcolor(title="Add Color" if SystemLanguage=="English" else "Додати колір")
            if ChoosenColor != (None, None) and ChoosenColor[0] not in AddColorsSetRgb:
                AddColorsSetRgb.append(ChoosenColor[0])
                OpenAddColorsSetSettingsWindow()

        IBNGWindow.after(100, GoToAnotherPage)
        


def AddColorPaletteButtonOnEnter(Event):
   global IsEnterAddColorPaletteButton
   IsEnterAddColorPaletteButton=True

def AddColorPaletteButtonOnLeave(Event):
   global IsEnterAddColorPaletteButton
   IsEnterAddColorPaletteButton=False














def SaveAndUseButtonOnClick(Event):
    SaveAndUseButton['image'] = TkImages['SaveAndUseColorSetClamped']


def SaveAndUseButtonRelease(Event):
    SaveAndUseButton['image'] = TkImages['SaveAndUseColorSetRealesed']
    if IsEnterSaveAndUseButton == True:
        def GoToAnotherPage():
            global StockColorsSetName
            global StockColorsSets
            global ColorsStock
            if AddColorsSetSettingsText.get() in str(open(ApplicationPath+'/Cash/StockColorsSets.txt', 'r').read()) and ColorSetMode==0:
                showwarning('Save error' if SystemLanguage=="English" else "Помилка збереження", 'The exact same color set already exsists!' if SystemLanguage=="English" else 'Такий самий набір кольорів уже існує!')
            elif AddColorsSetSettingsText.get().replace(' ', '')=='':
                showwarning('Save error' if SystemLanguage=="English" else "Помилка збереження", 'The name can`t be empty!' if SystemLanguage=="English" else "Ім'я не може бути порожнім!")
            elif len(AddColorsSetRgb)<=8:
                showwarning('Save error' if SystemLanguage=="English" else "Помилка збереження", 'The number of colors must be more than 8!' if SystemLanguage=="English" else "Кількість кольорів має бути більше 8!")
            elif len(AddColorsSetRgb)>80:
                showwarning('Save error' if SystemLanguage=="English" else "Помилка збереження", 'The number of colors must be less than 80!' if SystemLanguage=="English" else "Кількість кольорів має бути менше 80!")
            else:
                StockColorsSetName=AddColorsSetSettingsText.get()
                ColorsStock=AddColorsSetRgb
                if ColorSetMode==0:
                    open(ApplicationPath+'/Cash/StockColorsSets.txt', 'a').write(f'\n{StockColorsSetName}:{ColorsStock}')
                else:
                    open(ApplicationPath+'/Cash/StockColorsSets.txt', 'w').write(StockColorsSets.replace(StockColorsSets.split('\n')[ColorSetNameForEdit], f'{StockColorsSetName}:{ColorsStock}'))
                open(ApplicationPath+'/Cash/StockColorsSet.txt', 'w').write(StockColorsSetName)
                
                StockColorsSets=str(open(ApplicationPath+'/Cash/StockColorsSets.txt', 'r').read())
                OpenChangeColorSetsWindow()

        IBNGWindow.after(100, GoToAnotherPage)
        


def SaveAndUseButtonOnEnter(Event):
   global IsEnterSaveAndUseButton
   IsEnterSaveAndUseButton=True

def SaveAndUseButtonOnLeave(Event):
   global IsEnterSaveAndUseButton
   IsEnterSaveAndUseButton=False










def SaveColorSetButtonOnClick(Event):
    SaveButton['image'] = TkImages['SaveColorSetClamped']


def SaveColorSetButtonRelease(Event):
    SaveButton['image'] = TkImages['SaveColorSetRealesed']
    if IsEnterSaveButton == True:
        def GoToAnotherPage():
            global StockColorsSets
            global ColorsStock
            global StockColorsSetName
            if AddColorsSetSettingsText.get() in str(open(ApplicationPath+'/Cash/StockColorsSets.txt', 'r').read()) and ColorSetMode==0:
                showwarning('Save error' if SystemLanguage=="English" else "Помилка збереження", 'The exact same color set already exsists!' if SystemLanguage=="English" else 'Такий самий набір кольорів уже існує!')
            elif AddColorsSetSettingsText.get().replace(' ', '')=='':
                showwarning('Save error' if SystemLanguage=="English" else "Помилка збереження", 'The name can`t be empty!' if SystemLanguage=="English" else "Ім'я не може бути порожнім!")
            elif len(AddColorsSetRgb)<=8:
                showwarning('Save error' if SystemLanguage=="English" else "Помилка збереження", 'The number of colors must be more than 8!' if SystemLanguage=="English" else "Кількість кольорів має бути більше 8!")
            elif len(AddColorsSetRgb)>80:
                showwarning('Save error' if SystemLanguage=="English" else "Помилка збереження", 'The number of colors must be less than 80!' if SystemLanguage=="English" else "Кількість кольорів має бути менше 80!")
            else:
                if ColorSetMode==0:
                    open(ApplicationPath+'/Cash/StockColorsSets.txt', 'a').write(f'\n{AddColorsSetSettingsText.get()}:{AddColorsSetRgb}')
                elif ColorSetMode==1:
                    open(ApplicationPath+'/Cash/StockColorsSets.txt', 'w').write(StockColorsSets.replace(StockColorsSets.split('\n')[ColorSetNameForEdit], f'{AddColorsSetSettingsText.get()}:{AddColorsSetRgb}'))
                elif ColorSetMode==2:
                    open(ApplicationPath+'/Cash/StockColorsSets.txt', 'w').write(StockColorsSets.replace(StockColorsSets.split('\n')[ColorSetNameForEdit], f'{AddColorsSetSettingsText.get()}:{AddColorsSetRgb}'))
                    open(ApplicationPath+'/Cash/StockColorsSet.txt', 'w').write(AddColorsSetSettingsText.get())
                    ColorsStock=AddColorsSetRgb
                    StockColorsSetName=AddColorsSetSettingsText.get()
                
                StockColorsSets=str(open(ApplicationPath+'/Cash/StockColorsSets.txt', 'r').read())
                OpenChangeColorSetsWindow()

        IBNGWindow.after(100, GoToAnotherPage)
        


def SaveColorSetButtonOnEnter(Event):
   global IsEnterSaveButton
   IsEnterSaveButton=True

def SaveColorSetButtonOnLeave(Event):
   global IsEnterSaveButton
   IsEnterSaveButton=False






def DeleteColorSetButtonOnClick(Event):
    DeleteButton['image'] = TkImages['DeleteColorSetClamped']


def DeleteColorSetButtonRelease(Event):
    DeleteButton['image'] = TkImages['DeleteColorSetRealesed']
    if IsEnterDeleteButton == True:
        def GoToAnotherPage():
            global StockColorsSets
            global ColorsStock
            global StockColorsSetName
            open(ApplicationPath+'/Cash/StockColorsSets.txt', 'w').write(StockColorsSets.replace('\n'+StockColorsSets.split('\n')[ColorSetNameForEdit], ''))
                  
            StockColorsSets=str(open(ApplicationPath+'/Cash/StockColorsSets.txt', 'r').read()) 
            if ColorSetMode==2:
                StockColorsSets=str(open(ApplicationPath+'/Cash/StockColorsSets.txt', 'r').read())
                StockColorsSetName=StockColorsSets.split('\n')[0][:StockColorsSets.split('\n')[0].find(':')]
                for StockColorsSet in StockColorsSets.split('\n'):
                    if StockColorsSetName in StockColorsSet:
                        ColorsStock=ast.literal_eval(StockColorsSet[StockColorsSet.find(':')+1:])
                        break
                open(ApplicationPath+'/Cash/StockColorsSet.txt', 'w').write(StockColorsSetName)
            OpenChangeColorSetsWindow()

        IBNGWindow.after(100, GoToAnotherPage)
        


def DeleteColorSetButtonOnEnter(Event):
   global IsEnterDeleteButton
   IsEnterDeleteButton=True

def DeleteColorSetButtonOnLeave(Event):
   global IsEnterDeleteButton
   IsEnterDeleteButton=False

   

def OpenAddColorsSetSettingsWindow():
    global Widgets
    global ScrollCanvas
    global ScrollFrame
    global ColorsSetByWidth
    global AddColorsSetSettingsText
    global PaletteAddColorDeleteButtonRealesed
    global PaletteAddColorDeleteButtonClamped
    global PaletteAddColorClamped
    global AddColorsSetRgb
    global ScrollbarColorsSet
    global AddColorPaletteButton
    global ColorSetName
    global SaveAndUseButton
    global SaveButton
    global DeleteButton
    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
    [IBNGWindow.unbind_all(Event) for Event in Bindings]
    [IBNGWindow.unbind(Event) for Event in Bindings]
    for WindowElement in IBNGWindow.winfo_children():
       WindowElement.destroy()
    WidgetsInWindow=['BackgroundDetail3', 'ColorSetsText', 'BackButton']
    Widgets = {WidgetInformation[0]: Label(IBNGWindow, image=WidgetInformation[1], bg="#"+WidgetInformation[2], bd=0) for WidgetInformation in WidgetsInformation if WidgetInformation[0] in WidgetsInWindow}

    IBNGWindow.update()

    PaletteAddColorDeleteButtonRealesed=[]
    PaletteAddColorDeleteButtonClamped=[]
    PaletteAddColorClamped=[]
    

    Widgets['BackgroundDetail3'].place(y=-10, rely=0, relx=0.5, anchor='n')


        
    AddColorsSetSettingsText = Entry(IBNGWindow, font=("Arial", 40, "bold"), justify='center', bg="#fff7d9", borderwidth=0, highlightthickness=2, highlightbackground='#ffb000', highlightcolor='#ffb000', fg='#ffb000', insertbackground='#ffb000')
    AddColorsSetSettingsText.place(y=0, relx=0.5, rely=0, anchor='n', height=87, width=500)
    AddColorsSetSettingsText.insert("end", ColorSetName)
    def SetColorSetName(Event):
        global ColorSetName
        ColorSetName=AddColorsSetSettingsText.get()
        
    AddColorsSetSettingsText.bind("<KeyRelease>", SetColorSetName)




    Widgets['BackButton'].place(x=40, y=18, relx=0, rely=0, anchor='nw')

    Widgets['BackButton'].bind('<Enter>', BackButtonOnEnter)
    Widgets['BackButton'].bind('<Leave>', BackButtonOnLeave)
    Widgets['BackButton'].bind("<Button-1>", BackButtonOnClick)
    Widgets['BackButton'].bind("<ButtonRelease-1>", lambda Event:BackButtonRelease(Event, OpenChangeColorSetsWindow))








    ColorsSetScrollCanvas=Canvas(IBNGWindow, height=int(IBNGWindow.winfo_height()-87), width=IBNGWindow.winfo_width(), bg="#fff9e9", bd=0, highlightbackground="#fff9e9")
    ColorsSetScrollCanvas.place(y=87, relx=0.5, rely=0, anchor='n')

    ColorsSetByWidth=int(IBNGWindow.winfo_width()/120)
    
    ColorsSetScrollFrame=Frame(ColorsSetScrollCanvas, height=((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+260 if ColorSetMode==1 else ((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+180, width=IBNGWindow.winfo_width(), bg="#fff9e9")

    ColorsSetScrollCanvas.create_window((0,0), window=ColorsSetScrollFrame, anchor="nw")



    AddColorsSetWidget=[]
    
    for IndexAddColorsSet, AddColorsSet in enumerate(['Add']+AddColorsSetRgb):
        AddColorSetRow=math.ceil((IndexAddColorsSet+1)/ColorsSetByWidth)-1
        AddColorSetColumn=IndexAddColorsSet-(AddColorSetRow*ColorsSetByWidth)
        if IndexAddColorsSet==0:
            AddColorPaletteButton=Label(ColorsSetScrollFrame, image=TkImages['AddColorPaletteRealesed'], bg="#fff9e9", bd=0)
            AddColorPaletteButton.place(x=20, y=20, relx=0, rely=0, anchor='nw')
            AddColorPaletteButton.bind('<Enter>', AddColorPaletteButtonOnEnter)
            AddColorPaletteButton.bind('<Leave>', AddColorPaletteButtonOnLeave)
            AddColorPaletteButton.bind("<Button-1>", AddColorPaletteButtonOnClick)
            AddColorPaletteButton.bind("<ButtonRelease-1>", AddColorPaletteButtonRelease)
        else:
            IndexAddColorsSet-=1
            AddColorSetImage=Image.new('RGBA', (710, 710), color = (255, 255, 255,0))
            AddColorSetImageDraw=ImageDraw.Draw(AddColorSetImage)
            AddColorSetImageDraw.rectangle([(30, 30), (675, 675)], fill=AddColorsSet)
            AddColorSetImage.paste(Image.open(GetDataFilePath('English/PaletteAddColorDeleteButtonRealesed.png')), (0, 0), mask=Image.open(GetDataFilePath('English/PaletteAddColorDeleteButtonRealesed.png')))
            if len(str(IndexAddColorsSet+1))==1:
                AddColorSetImageDraw.text((90, 35), str(IndexAddColorsSet+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))
            else:
                AddColorSetImageDraw.text((30, 35), str(IndexAddColorsSet+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))

            PaletteAddColorDeleteButtonRealesed.append(ImageTk.PhotoImage(AddColorSetImage.resize((80, 80))))

            AddColorSetImage=Image.new('RGBA', (710, 710), color = (255, 255, 255,0))
            AddColorSetImageDraw=ImageDraw.Draw(AddColorSetImage)
            AddColorSetImageDraw.rectangle([(30, 30), (675, 675)], fill=AddColorsSet)
            AddColorSetImage.paste(Image.open(GetDataFilePath('English/PaletteAddColorDeleteButtonClamped.png')), (0, 0), mask=Image.open(GetDataFilePath('English/PaletteAddColorDeleteButtonClamped.png')))
            if len(str(IndexAddColorsSet+1))==1:
                AddColorSetImageDraw.text((90, 35), str(IndexAddColorsSet+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))
            else:
                AddColorSetImageDraw.text((30, 35), str(IndexAddColorsSet+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))

            PaletteAddColorDeleteButtonClamped.append(ImageTk.PhotoImage(AddColorSetImage.resize((80, 80))))

            AddColorSetImage=Image.new('RGBA', (710, 710), color = (255, 255, 255,0))
            AddColorSetImageDraw=ImageDraw.Draw(AddColorSetImage)
            AddColorSetImageDraw.rectangle([(30, 30), (675, 675)], fill=AddColorsSet)
            AddColorSetImage.paste(Image.open(GetDataFilePath('English/PaletteAddColorClamped.png')), (0, 0), mask=Image.open(GetDataFilePath('English/PaletteAddColorClamped.png')))
            if len(str(IndexAddColorsSet+1))==1:
                AddColorSetImageDraw.text((90, 35), str(IndexAddColorsSet+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))
            else:
                AddColorSetImageDraw.text((30, 35), str(IndexAddColorsSet+1), font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 200), fill=(255, 173, 0, 255))

            PaletteAddColorClamped.append(ImageTk.PhotoImage(AddColorSetImage.resize((80, 80))))


            AddColorsSetWidget.append(Label(ColorsSetScrollFrame, image=PaletteAddColorDeleteButtonRealesed[IndexAddColorsSet], bg="#fff9e9", bd=0))
            AddColorsSetWidget[IndexAddColorsSet].place(x=AddColorSetColumn*120+20, y=20+(AddColorSetRow*120), relx=0, rely=0, anchor='nw')
            AddColorsSetWidget[IndexAddColorsSet].bind("<Button-1>", lambda Event, IndexAddColorsSet=IndexAddColorsSet:AddColorsSetWidgetOnClick(Event, IndexAddColorsSet))
            AddColorsSetWidget[IndexAddColorsSet].bind("<ButtonRelease-1>", lambda Event, IndexAddColorsSet=IndexAddColorsSet:AddColorsSetWidgetRelease(Event, IndexAddColorsSet))


    if ColorSetMode==0:
        SaveAndUseButton=Label(ColorsSetScrollFrame, image=TkImages['SaveAndUseColorSetRealesed'], bg="#fff9e9", bd=0)
        SaveAndUseButton.place(x=0, y=((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+20, relx=0.5, rely=0, anchor='n')
        SaveAndUseButton.bind('<Enter>', SaveAndUseButtonOnEnter)
        SaveAndUseButton.bind('<Leave>', SaveAndUseButtonOnLeave)
        SaveAndUseButton.bind("<Button-1>", SaveAndUseButtonOnClick)
        SaveAndUseButton.bind("<ButtonRelease-1>", SaveAndUseButtonRelease)


        SaveButton=Label(ColorsSetScrollFrame, image=TkImages['SaveColorSetRealesed'], bg="#fff9e9", bd=0)
        SaveButton.place(x=0, y=((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+100, relx=0.5, rely=0, anchor='n')
        SaveButton.bind('<Enter>', SaveColorSetButtonOnEnter)
        SaveButton.bind('<Leave>', SaveColorSetButtonOnLeave)
        SaveButton.bind("<Button-1>", SaveColorSetButtonOnClick)
        SaveButton.bind("<ButtonRelease-1>", SaveColorSetButtonRelease)
    elif ColorSetMode==1:
        SaveAndUseButton=Label(ColorsSetScrollFrame, image=TkImages['SaveAndUseColorSetRealesed'], bg="#fff9e9", bd=0)
        SaveAndUseButton.place(x=0, y=((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+20, relx=0.5, rely=0, anchor='n')
        SaveAndUseButton.bind('<Enter>', SaveAndUseButtonOnEnter)
        SaveAndUseButton.bind('<Leave>', SaveAndUseButtonOnLeave)
        SaveAndUseButton.bind("<Button-1>", SaveAndUseButtonOnClick)
        SaveAndUseButton.bind("<ButtonRelease-1>", SaveAndUseButtonRelease)


        SaveButton=Label(ColorsSetScrollFrame, image=TkImages['SaveColorSetRealesed'], bg="#fff9e9", bd=0)
        SaveButton.place(x=0, y=((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+100, relx=0.5, rely=0, anchor='n')
        SaveButton.bind('<Enter>', SaveColorSetButtonOnEnter)
        SaveButton.bind('<Leave>', SaveColorSetButtonOnLeave)
        SaveButton.bind("<Button-1>", SaveColorSetButtonOnClick)
        SaveButton.bind("<ButtonRelease-1>", SaveColorSetButtonRelease)


        DeleteButton=Label(ColorsSetScrollFrame, image=TkImages['DeleteColorSetRealesed'], bg="#fff9e9", bd=0)
        DeleteButton.place(x=0, y=((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+180, relx=0.5, rely=0, anchor='n')
        DeleteButton.bind('<Enter>', DeleteColorSetButtonOnEnter)
        DeleteButton.bind('<Leave>', DeleteColorSetButtonOnLeave)
        DeleteButton.bind("<Button-1>", DeleteColorSetButtonOnClick)
        DeleteButton.bind("<ButtonRelease-1>", DeleteColorSetButtonRelease)
    elif ColorSetMode==2:
        SaveButton=Label(ColorsSetScrollFrame, image=TkImages['SaveColorSetRealesed'], bg="#fff9e9", bd=0)
        SaveButton.place(x=0, y=((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+20, relx=0.5, rely=0, anchor='n')
        SaveButton.bind('<Enter>', SaveColorSetButtonOnEnter)
        SaveButton.bind('<Leave>', SaveColorSetButtonOnLeave)
        SaveButton.bind("<Button-1>", SaveColorSetButtonOnClick)
        SaveButton.bind("<ButtonRelease-1>", SaveColorSetButtonRelease)


        DeleteButton=Label(ColorsSetScrollFrame, image=TkImages['DeleteColorSetRealesed'], bg="#fff9e9", bd=0)
        DeleteButton.place(x=0, y=((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+100, relx=0.5, rely=0, anchor='n')
        DeleteButton.bind('<Enter>', DeleteColorSetButtonOnEnter)
        DeleteButton.bind('<Leave>', DeleteColorSetButtonOnLeave)
        DeleteButton.bind("<Button-1>", DeleteColorSetButtonOnClick)
        DeleteButton.bind("<ButtonRelease-1>", DeleteColorSetButtonRelease)

    ColorsSetScrollCanvas.bind('<Configure>', lambda Event:ColorsSetScrollCanvas.configure(scrollregion=(0, 0, 1800, ((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+260 if ColorSetMode==1 else ((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+180)))







    def IncreaseTimer():
        global ScrollbarColorsSetHideTimer
        global ScrollbarColorsSetHide
        ScrollbarColorsSetHideTimer+=1
        if ScrollbarColorsSetHideTimer>50000 and ScrollbarColorsSetHide==True:
          if ScrollbarColorsSet.winfo_exists():
              ScrollbarColorsSet.place_forget()
        else:
          IBNGWindow.after(1, IncreaseTimer)

    def MouseScrollbarColorsSet(Event):
        global ScrollbarColorsSetHideTimer
        global ScrollbarColorsSetHide
        if Event.keysym=='Down' or Event.keysym=='Up':
            Force=-(1/((len(AddColorsSetRgb)+1))) if Event.keysym=='Up' else (1/(len(AddColorsSetRgb)))
            ColorsSetScrollCanvas.yview_moveto(ColorsSetScrollCanvas.yview()[0]+Force if ColorsSetScrollCanvas.yview()[0]+Force > 0 else 0)
        else:
            Force=-(1/((len(AddColorsSetRgb)+1)*10)*Event.delta)
            ColorsSetScrollCanvas.yview_moveto(ColorsSetScrollCanvas.yview()[0]+Force if ColorsSetScrollCanvas.yview()[0]+Force > 0 else 0)



        if ScrollbarColorsSet.place_info()=={}:
            ScrollbarColorsSet.place( x=0, y=42, relx=1, rely=0.5, anchor='e', height=int(IBNGWindow.winfo_height()-89) )
        ScrollbarColorsSetHideTimer=0
        ScrollbarColorsSetHide=True
        IBNGWindow.after(1, IncreaseTimer)

    ColorsSetScrollCanvas.bind_all('<MouseWheel>', MouseScrollbarColorsSet)
    IBNGWindow.bind("<Up>", MouseScrollbarColorsSet)
    IBNGWindow.bind("<Down>", MouseScrollbarColorsSet)


    ScrollbarColorsSet=ttk.Scrollbar(IBNGWindow, orient='vertical', command=ColorsSetScrollCanvas.yview)


    ScrollbarStyle = ThemedStyle(ScrollbarColorsSet)

    ScrollbarStyle.set_theme("arc")

    def FocusInScrollbar(Event):
        global ScrollbarColorsSetHideTimer
        global ScrollbarColorsSetHide
        ScrollbarColorsSetHideTimer=0
        ScrollbarColorsSetHide=False



    def FocusOutScrollbar(Event):
        global ScrollbarColorsSetHideTimer
        global ScrollbarColorsSetHide
        ScrollbarColorsSetHideTimer=0
        ScrollbarColorsSetHide=True




    ScrollbarColorsSet.bind('<Button-1>', FocusInScrollbar)

    ScrollbarColorsSet.bind('<ButtonRelease-1>', FocusOutScrollbar)


    ColorsSetScrollCanvas.configure(yscrollcommand=ScrollbarColorsSet.set)











    def OnWindowResize(Event):
        global ColorsSetByWidth
        ColorsSetByWidthNow=int((IBNGWindow.winfo_width())/120)
        ColorsSetScrollCanvas.configure(height=int(IBNGWindow.winfo_height())-89, width=IBNGWindow.winfo_width())
        ColorsSetScrollFrame.configure(width=IBNGWindow.winfo_width())
        if ScrollbarColorsSet.place_info()!={}:
            ScrollbarColorsSet.place( x=0, y=42, relx=1, rely=0.5, anchor='e', height=int(IBNGWindow.winfo_height()-89) )
        if ColorsSetByWidth!=ColorsSetByWidthNow:
            ColorsSetScrollFrame['height']=((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+260 if ColorSetMode==1 else ((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+180

            for IndexAddColorsSet, AddColorsSet in enumerate(AddColorsSetRgb):
                IndexAddColorsSet+=1
                AddColorSetRow=math.ceil((IndexAddColorsSet+1)/ColorsSetByWidthNow)-1
                AddColorSetColumn=IndexAddColorsSet-(AddColorSetRow*ColorsSetByWidthNow)
                IndexAddColorsSet-=1
                
                AddColorsSetWidget[IndexAddColorsSet].place(x=AddColorSetColumn*120+20, y=20+(AddColorSetRow*120), relx=0, rely=0, anchor='nw')
            

            if ColorSetMode==0:
                SaveAndUseButton.place(x=0, y=((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+20, relx=0.5, rely=0, anchor='n')
                SaveButton.place(x=0, y=((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+100, relx=0.5, rely=0, anchor='n')
            elif ColorSetMode==1:
                SaveAndUseButton.place(x=0, y=((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+20, relx=0.5, rely=0, anchor='n')
                SaveButton.place(x=0, y=((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+100, relx=0.5, rely=0, anchor='n')
                DeleteButton.place(x=0, y=((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+180, relx=0.5, rely=0, anchor='n')
            elif ColorSetMode==2:
                SaveButton.place(x=0, y=((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+20, relx=0.5, rely=0, anchor='n')
                DeleteButton.place(x=0, y=((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+100, relx=0.5, rely=0, anchor='n')
                        
            ColorsSetScrollCanvas.bind('<Configure>', lambda Event:ColorsSetScrollCanvas.configure(scrollregion=(0, 0, 1800, ((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+260 if ColorSetMode==1 else ((math.ceil((len(AddColorsSetRgb)+1)/ColorsSetByWidth))*120)+180)))
            ColorsSetByWidth=ColorsSetByWidthNow
          
             
    IBNGWindow.bind("<Configure>", OnWindowResize)
















def OpenChangeColorSetsWindow():
    global Widgets
    global ScrollCanvas
    global ScrollFrame
    global Scrollbar
    global StockColorsSetsRealesedImageTk
    global StockColorsSetsClampedImageTk
    global StockColorsSetsUsedImageTk
    global StockColorsSetsUsedClampedImageTk
    global StockColorsSetsUsedIndex
    global StockColorsSetsWidget
    global AddColorSetSettingsPlaceButton
    global IsEnterStockColorSets
    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
    [IBNGWindow.unbind_all(Event) for Event in Bindings]
    [IBNGWindow.unbind(Event) for Event in Bindings]
    for WindowElement in IBNGWindow.winfo_children():
       WindowElement.destroy()
    WidgetsInWindow=['BackgroundDetail3', 'ColorSetsText', 'BackButton']
    Widgets = {WidgetInformation[0]: Label(IBNGWindow, image=WidgetInformation[1], bg="#"+WidgetInformation[2], bd=0) for WidgetInformation in WidgetsInformation if WidgetInformation[0] in WidgetsInWindow}

    IBNGWindow.update()
    

    Widgets['BackgroundDetail3'].place(y=-10, rely=0, relx=0.5, anchor='n')


    Widgets['ColorSetsText'].place(y=21, relx=0.5, anchor='n')






    ScrollCanvas=Canvas(IBNGWindow, height=int(IBNGWindow.winfo_height()-87), width=600, bg="#fff9e9", bd=0, highlightbackground="#fff9e9")
    ScrollCanvas.place(y=87, relx=0.5, rely=0, anchor='n')

    ScrollFrame=Frame(ScrollCanvas, height=107+(len(StockColorsSets.split('\n'))*74), width=600, bg="#fff9e9")


    ScrollCanvas.create_window((0,0), window=ScrollFrame, anchor="nw")













    StockColorsSetsRealesedImageTk=[]
    StockColorsSetsClampedImageTk=[]
    StockColorsSetsUsedImageTk=[]
    StockColorsSetsUsedClampedImageTk=[]
    StockColorsSetsWidget=[]
    IsEnterStockColorSets=[]
    for StockColorsSetIndex, StockColorsSet in enumerate(StockColorsSets.split('\n')):
        StockColorsSet=StockColorsSet[:StockColorsSet.find(':')]
        ColorSetSettingsPlaceButtonRealesed=PillowImages['ColorSetSettingsPlaceButtonRealesed'].copy()
        ColorSetSettingsPlaceButtonRealesedDraw=ImageDraw.Draw(ColorSetSettingsPlaceButtonRealesed)
        StockColorsSetSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28).getbbox(StockColorsSet)
        StockColorsSetWidth, StockColorsSetHeight=StockColorsSetSize[2]-StockColorsSetSize[0], StockColorsSetSize[3]+StockColorsSetSize[1]
        
        if StockColorsSetWidth<430:
            StockColorsSetText=StockColorsSet
        else:
            StockColorsSetText=StockColorsSet
            while StockColorsSetWidth>=430:
                StockColorsSetSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28).getbbox(StockColorsSetText+'...')
                StockColorsSetWidth, StockColorsSetHeight=StockColorsSetSize[2]-StockColorsSetSize[0], StockColorsSetSize[3]+StockColorsSetSize[1]
                StockColorsSetText=StockColorsSetText[:-1]
            StockColorsSetText+='...'
            
        StockColorsSetWidth, StockColorsSetHeight=422-StockColorsSetWidth, math.ceil((61-StockColorsSetHeight)/2)
        ColorSetSettingsPlaceButtonRealesedDraw.text((23, StockColorsSetHeight), StockColorsSetText, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28), fill=(255, 198, 72, 255))
        StockColorsSetsRealesedImageTk.append(ImageTk.PhotoImage(ColorSetSettingsPlaceButtonRealesed))
        
        ColorSetSettingsPlaceButtonClamped=PillowImages['ColorSetSettingsPlaceButtonClamped'].copy()
        ColorSetSettingsPlaceButtonClampedDraw=ImageDraw.Draw(ColorSetSettingsPlaceButtonClamped)
        ColorSetSettingsPlaceButtonClampedDraw.text((23, StockColorsSetHeight), StockColorsSetText, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28), fill=(255, 198, 72, 255))
        StockColorsSetsClampedImageTk.append(ImageTk.PhotoImage(ColorSetSettingsPlaceButtonClamped))
        
        ColorSetSettingsPlaceButtonUsed=PillowImages['ColorSetSettingsPlaceButtonUsed'].copy()
        ColorSetSettingsPlaceButtonUsedDraw=ImageDraw.Draw(ColorSetSettingsPlaceButtonUsed)
        ColorSetSettingsPlaceButtonUsedDraw.text((23, StockColorsSetHeight-4), StockColorsSetText, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28), fill=(255, 198, 72, 255))
        StockColorsSetsUsedImageTk.append(ImageTk.PhotoImage(ColorSetSettingsPlaceButtonUsed))
        
        ColorSetSettingsPlaceButtonUsedClamped=PillowImages['ColorSetSettingsPlaceButtonUsedClamped'].copy()
        ColorSetSettingsPlaceButtonUsedClampedDraw=ImageDraw.Draw(ColorSetSettingsPlaceButtonUsedClamped)
        ColorSetSettingsPlaceButtonUsedClampedDraw.text((23, StockColorsSetHeight-4), StockColorsSetText, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28), fill=(255, 198, 72, 255))
        StockColorsSetsUsedClampedImageTk.append(ImageTk.PhotoImage(ColorSetSettingsPlaceButtonUsedClamped))

        if StockColorsSet != StockColorsSetName:
            StockColorsSetsWidget.append(Label(ScrollFrame, image=StockColorsSetsRealesedImageTk[-1], bg="#fff9e9", bd=0))
            StockColorsSetsWidget[-1].place(x=0, y=23+(StockColorsSetIndex*74), relx=0.5, rely=0, anchor='n')
            IsEnterStockColorSets.append(False)
            StockColorsSetsWidget[-1].bind('<Enter>', lambda Event, ColorSetIndex=StockColorsSetIndex:ColorsSetSettingsOnEnter(Event, ColorSetIndex))
            StockColorsSetsWidget[-1].bind('<Leave>', lambda Event, ColorSetIndex=StockColorsSetIndex:ColorsSetSettingsOnLeave(Event, ColorSetIndex))
            StockColorsSetsWidget[-1].bind("<Button-1>", lambda Event, ColorSetIndex=StockColorsSetIndex:ColorsSetSettingsOnClick(Event, ColorSetIndex))
            StockColorsSetsWidget[-1].bind("<ButtonRelease-1>", lambda Event, ColorSetIndex=StockColorsSetIndex:ColorsSetSettingsRelease(Event, ColorSetIndex))
        else:
            StockColorsSetsWidget.append(Label(ScrollFrame, image=StockColorsSetsUsedImageTk[-1], bg="#fff9e9", bd=0))
            StockColorsSetsWidget[-1].place(x=0, y=23+(StockColorsSetIndex*74), relx=0.5, rely=0, anchor='n')
            StockColorsSetsUsedIndex=StockColorsSetIndex
            IsEnterStockColorSets.append(False)
            StockColorsSetsWidget[-1].bind('<Enter>', lambda Event, ColorSetIndex=StockColorsSetIndex:ColorsSetSettingsOnEnter(Event, ColorSetIndex))
            StockColorsSetsWidget[-1].bind('<Leave>', lambda Event, ColorSetIndex=StockColorsSetIndex:ColorsSetSettingsOnLeave(Event, ColorSetIndex))
            StockColorsSetsWidget[-1].bind("<Button-1>", lambda Event, ColorSetIndex=StockColorsSetIndex:ColorsSetSettingsOnClick(Event, ColorSetIndex))
            StockColorsSetsWidget[-1].bind("<ButtonRelease-1>", lambda Event, ColorSetIndex=StockColorsSetIndex:ColorsSetSettingsRelease(Event, ColorSetIndex))

    AddColorSetSettingsPlaceButton=Label(ScrollFrame, image=TkImages['AddColorSetSettingsPlaceButtonRealesed'], bg="#fff9e9", bd=0)
    AddColorSetSettingsPlaceButton.place(x=0, y=23+(len(StockColorsSets.split('\n'))*74), relx=0.5, rely=0, anchor='n')
    AddColorSetSettingsPlaceButton.bind('<Enter>', AddColorsSetSettingsOnEnter)
    AddColorSetSettingsPlaceButton.bind('<Leave>', AddColorsSetSettingsOnLeave)
    AddColorSetSettingsPlaceButton.bind("<Button-1>", AddColorsSetSettingsOnClick)
    AddColorSetSettingsPlaceButton.bind("<ButtonRelease-1>", AddColorsSetSettingsRelease)


    







    ScrollCanvas.bind('<Configure>', lambda Event:ScrollCanvas.configure(scrollregion=(0, 0, 1000, 107+((len(StockColorsSets.split('\n'))+1)*74))))

    def IncreaseTimer():
        global ScrollbarHideTimer
        global ScrollbarHide
        ScrollbarHideTimer+=1
        if ScrollbarHideTimer>50000 and ScrollbarHide==True:
          if Scrollbar.winfo_exists():
              Scrollbar.place_forget()
        else:
          IBNGWindow.after(1, IncreaseTimer)

    def MouseScrollbar(Event):
        global ScrollbarHideTimer
        global ScrollbarHide
        if Event.keysym=='Down' or Event.keysym=='Up':
          Force=-(1/(len(CreatedImages)*30)) if Event.keysym=='Up' else (1/(len(CreatedImages)*30))
          ScrollCanvas.yview_moveto(ScrollCanvas.yview()[0]+Force if ScrollCanvas.yview()[0]+Force > 0 else 0)
        else:
          Force=-(1/(len(CreatedImages)*50)*Event.delta)
          ScrollCanvas.yview_moveto(ScrollCanvas.yview()[0]+Force if ScrollCanvas.yview()[0]+Force > 0 else 0)



        if Scrollbar.place_info()=={}:
            Scrollbar.place( x=0, y=40, relx=1, rely=0.5, anchor='e', height=int(IBNGWindow.winfo_height()-89) )
        ScrollbarHideTimer=0
        ScrollbarHide=True
        IBNGWindow.after(1, IncreaseTimer)
        

    ScrollCanvas.bind_all('<MouseWheel>', MouseScrollbar)
    IBNGWindow.bind("<Up>", MouseScrollbar)
    IBNGWindow.bind("<Down>", MouseScrollbar)


    Scrollbar=ttk.Scrollbar(IBNGWindow, orient='vertical', command=ScrollCanvas.yview)


    ScrollbarStyle = ThemedStyle(Scrollbar)

    ScrollbarStyle.set_theme("arc")

    def FocusInScrollbar(Event):
        global ScrollbarHideTimer
        global ScrollbarHide
        ScrollbarHideTimer=0
        ScrollbarHide=False



    def FocusOutScrollbar(Event):
        global ScrollbarHideTimer
        global ScrollbarHide
        ScrollbarHideTimer=0
        ScrollbarHide=True




    Scrollbar.bind('<Button-1>', FocusInScrollbar)

    Scrollbar.bind('<ButtonRelease-1>', FocusOutScrollbar)



    ScrollCanvas.configure(yscrollcommand=Scrollbar.set)




    




    Widgets['BackButton'].place(x=60, y=18, relx=0, rely=0, anchor='nw')

    Widgets['BackButton'].bind('<Enter>', BackButtonOnEnter)
    Widgets['BackButton'].bind('<Leave>', BackButtonOnLeave)
    Widgets['BackButton'].bind("<Button-1>", BackButtonOnClick)
    Widgets['BackButton'].bind("<ButtonRelease-1>", lambda Event:BackButtonRelease(Event, OpenSettingsWindow))




    def OnWindowResize(Event):
         ScrollCanvas.configure( height=int(IBNGWindow.winfo_height()-87) )
         if Scrollbar.place_info()!={}:
            Scrollbar.place( x=0, y=40, relx=1, rely=0.5, anchor='e', height=int(IBNGWindow.winfo_height()-89) )
      
         
    IBNGWindow.bind("<Configure>", OnWindowResize)



    










   


def OpenSettingsWindow():
    global Widgets
    global ExportText
    global DownloadFileFormat
    global ExportFormatPromptText
    global ColorsFromStockText
    global PriorityLanguageText
    global SystemLanguageWidth
    global SystemLanguageHeight
    global StockColorsSetNameWidth
    global StockColorsSetNameHeight
    global ScrollCanvas
    global ScrollFrame
    [WindowElement.unbind(Event) for WindowElement in IBNGWindow.winfo_children() for Event in Bindings]
    [IBNGWindow.unbind_all(Event) for Event in Bindings]
    [IBNGWindow.unbind(Event) for Event in Bindings]
    for WindowElement in IBNGWindow.winfo_children():
       WindowElement.destroy()
    WidgetsInWindow=['BackgroundDetail3', 'SettingsText', 'ThisPageIsNotAvailableYet', 'HomeButton']
    Widgets = {WidgetInformation[0]: Label(IBNGWindow, image=WidgetInformation[1], bg="#"+WidgetInformation[2], bd=0) for WidgetInformation in WidgetsInformation if WidgetInformation[0] in WidgetsInWindow}

    IBNGWindow.update()


    Widgets['BackgroundDetail3'].place(y=-10, rely=0, relx=0.5, anchor='n')


    Widgets['SettingsText'].place(y=18, relx=0.5, anchor='n')


    Widgets['HomeButton'].place(x=-27, y=12, relx=1, rely=0, anchor='ne')

    Widgets['HomeButton'].bind('<Enter>', HomeButtonOnEnter)
    Widgets['HomeButton'].bind('<Leave>', HomeButtonOnLeave)
    Widgets['HomeButton'].bind("<Button-1>", HomeButtonOnClick)
    Widgets['HomeButton'].bind("<ButtonRelease-1>", HomeButtonRelease)




    ScrollCanvas=Canvas(IBNGWindow, height=int(IBNGWindow.winfo_height()-87), width=600, bg="#fff9e9", bd=0, highlightbackground="#fff9e9")
    ScrollCanvas.place(y=87, relx=0.5, rely=0, anchor='n')

    ScrollFrame=Frame(ScrollCanvas, height=636, width=600, bg="#fff9e9")


    ScrollCanvas.create_window((0,0), window=ScrollFrame, anchor="nw")
















    PriorityLanguageText=Label(ScrollFrame, text="Priority language" if SystemLanguage=="English" else "Пріоритетна мова", bg="#fff9e9", fg="#ffc648", bd=0, font=("Arial", 28, "bold"))
    PriorityLanguageText.place(x=-216, y=65, relx=0.5, rely=0, anchor='nw')

    PriorityLanguageSettingsPlaceButtonRealesed=PillowImages['PriorityLanguageSettingsPlaceButtonRealesed'].copy()
    PriorityLanguageSettingsPlaceButtonRealesedDraw=ImageDraw.Draw(PriorityLanguageSettingsPlaceButtonRealesed)
    SystemLanguageSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28).getbbox(SystemLanguage)
    SystemLanguageWidth, SystemLanguageHeight=SystemLanguageSize[2]-SystemLanguageSize[0], SystemLanguageSize[3]+SystemLanguageSize[1]
    SystemLanguageWidth, SystemLanguageHeight=422-SystemLanguageWidth, math.ceil((61-SystemLanguageHeight)/2)
    PriorityLanguageSettingsPlaceButtonRealesedDraw.text((SystemLanguageWidth, SystemLanguageHeight), SystemLanguage, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28), fill=(255, 198, 72, 255))
    TkImages['PriorityLanguageSettingsPlaceButtonRealesed']=ImageTk.PhotoImage(PriorityLanguageSettingsPlaceButtonRealesed)

    Widgets['PriorityLanguageSettingsPlaceButton']=Label(ScrollFrame, image=TkImages['PriorityLanguageSettingsPlaceButtonRealesed'], bg="#fff9e9", bd=0)
    Widgets['PriorityLanguageSettingsPlaceButton'].place(x=0, y=107, relx=0.5, rely=0, anchor='n')
    Widgets['PriorityLanguageSettingsPlaceButton'].bind('<Enter>', LanguageSettingsOnEnter)
    Widgets['PriorityLanguageSettingsPlaceButton'].bind('<Leave>', LanguageSettingsOnLeave)
    Widgets['PriorityLanguageSettingsPlaceButton'].bind('<Button-1>', LanguageSettingsOnClick)
    Widgets['PriorityLanguageSettingsPlaceButton'].bind('<ButtonRelease-1>', LanguageSettingsRelease)





    
    ColorsFromStockText=Label(ScrollFrame, text="Colors from stock" if SystemLanguage=="English" else "Кольори зі складу", bg="#fff9e9", fg="#ffc648", bd=0, font=("Arial", 28, "bold"))
    ColorsFromStockText.place(x=-216, y=231, relx=0.5, rely=0, anchor='nw')
    

    ColorSetsSettingsPlaceButtonRealesed=PillowImages['ColorSetsSettingsPlaceButtonRealesed'].copy()
    ColorSetsSettingsPlaceButtonRealesedDraw=ImageDraw.Draw(ColorSetsSettingsPlaceButtonRealesed)
    StockColorsSetNameSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28).getbbox(StockColorsSetName)
    StockColorsSetNameWidth, StockColorsSetNameHeight=StockColorsSetNameSize[2]-StockColorsSetNameSize[0], StockColorsSetNameSize[3]+StockColorsSetNameSize[1]
      
    if StockColorsSetNameWidth<236:
        StockColorsSetNameText=StockColorsSetName
        StockColorsSetNameWidth, StockColorsSetNameHeight=422-StockColorsSetNameWidth, math.ceil((61-StockColorsSetNameHeight)/2)
    else:
        StockColorsSetNameText=StockColorsSetName
        while StockColorsSetNameWidth>=236:
            StockColorsSetNameSize=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28).getbbox(StockColorsSetNameText+'...')
            StockColorsSetNameWidth, StockColorsSetNameHeight=StockColorsSetNameSize[2]-StockColorsSetNameSize[0], StockColorsSetNameSize[3]+StockColorsSetNameSize[1]
            StockColorsSetNameText=StockColorsSetNameText[:-1]
        StockColorsSetNameText+='...'
        StockColorsSetNameWidth, StockColorsSetNameHeight=440-StockColorsSetNameWidth, math.ceil((61-StockColorsSetNameHeight)/2)
            
    
    ColorSetsSettingsPlaceButtonRealesedDraw.text((StockColorsSetNameWidth, StockColorsSetNameHeight), StockColorsSetNameText, font=ImageFont.truetype(GetDataFilePath("arialbd.ttf"), 28), fill=(255, 198, 72, 255))
    TkImages['ColorSetsSettingsPlaceButtonRealesed']=ImageTk.PhotoImage(ColorSetsSettingsPlaceButtonRealesed)

    Widgets['ColorSetsSettingsPlaceButton']=Label(ScrollFrame, image=TkImages['ColorSetsSettingsPlaceButtonRealesed'], bg="#fff9e9", bd=0)
    Widgets['ColorSetsSettingsPlaceButton'].place(x=0, y=273, relx=0.5, rely=0, anchor='n')
    Widgets['ColorSetsSettingsPlaceButton'].bind('<Enter>', ColorSetsSettingsOnEnter)
    Widgets['ColorSetsSettingsPlaceButton'].bind('<Leave>', ColorSetsSettingsOnLeave)
    Widgets['ColorSetsSettingsPlaceButton'].bind('<Button-1>', ColorSetsSettingsOnClick)
    Widgets['ColorSetsSettingsPlaceButton'].bind('<ButtonRelease-1>', ColorSetsSettingsRelease)

    















    ScrollCanvas.bind('<Configure>', lambda Event:ScrollCanvas.configure(scrollregion=(0, 0, 1000, 636)))

    def IncreaseTimer():
        global ScrollbarHideTimer
        global ScrollbarHide
        ScrollbarHideTimer+=1
        if ScrollbarHideTimer>50000 and ScrollbarHide==True:
          if Scrollbar.winfo_exists():
              Scrollbar.place_forget()
        else:
          IBNGWindow.after(1, IncreaseTimer)

    def MouseScrollbar(Event):
        global ScrollbarHideTimer
        global ScrollbarHide
        if Event.keysym=='Down' or Event.keysym=='Up':
          Force=-(1/(len(CreatedImages)*30)) if Event.keysym=='Up' else (1/(len(CreatedImages)*30))
          ScrollCanvas.yview_moveto(ScrollCanvas.yview()[0]+Force if ScrollCanvas.yview()[0]+Force > 0 else 0)
        else:
          Force=-(1/(len(CreatedImages)*50)*Event.delta)
          ScrollCanvas.yview_moveto(ScrollCanvas.yview()[0]+Force if ScrollCanvas.yview()[0]+Force > 0 else 0)



        if Scrollbar.place_info()=={}:
            Scrollbar.place( x=0, y=40, relx=1, rely=0.5, anchor='e', height=int(IBNGWindow.winfo_height()-89) )
            ScrollbarHideTimer=0
            ScrollbarHide=True
            IBNGWindow.after(1, IncreaseTimer)

    ScrollCanvas.bind_all('<MouseWheel>', MouseScrollbar)
    IBNGWindow.bind("<Up>", MouseScrollbar)
    IBNGWindow.bind("<Down>", MouseScrollbar)


    Scrollbar=ttk.Scrollbar(IBNGWindow, orient='vertical', command=ScrollCanvas.yview)


    ScrollbarStyle = ThemedStyle(Scrollbar)

    ScrollbarStyle.set_theme("arc")

    def FocusInScrollbar(Event):
      global ScrollbarHideTimer
      global ScrollbarHide
      ScrollbarHideTimer=0
      ScrollbarHide=False



    def FocusOutScrollbar(Event):
      global ScrollbarHideTimer
      global ScrollbarHide
      ScrollbarHideTimer=0
      ScrollbarHide=True




    Scrollbar.bind('<Button-1>', FocusInScrollbar)

    Scrollbar.bind('<ButtonRelease-1>', FocusOutScrollbar)


    ScrollCanvas.configure(yscrollcommand=Scrollbar.set)





   
    def OnWindowResize(Event):
         ScrollCanvas.configure( height=int(IBNGWindow.winfo_height()-87) )
         if Scrollbar.place_info()!={}:
            Scrollbar.place( x=0, y=40, relx=1, rely=0.5, anchor='e', height=int(IBNGWindow.winfo_height()-89) )
      
         
    IBNGWindow.bind("<Configure>", OnWindowResize)
    
    #open(ApplicationPath+'/Cash/DownloadFileFormat.txt', 'w').write('.png')
    #DownloadFileFormat=str(open(ApplicationPath+'/Cash/DownloadFileFormat.txt', 'r').read())





   


















   








   
    





OpenStartWindow()

IBNGWindow.mainloop()
