import os
import glob
from dbr import *


async def detectBarcode(path):
    # if __name__ == "__main__":
    
    try:
        barcode_data=[]
        # 1.Initialize license.
        # The string "DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9" here is a free public trial license. Note that network connection is required for this license to work.
        # You can also request a 30-day trial license in the customer portal: https://www.dynamsoft.com/customer/license/trialLicense?architecture=dcv&product=dbr&utm_source=samples&package=python
        error = BarcodeReader.init_license("t0068lQAAAKxyE8pLl1+xIccoJF1r8MO85prSXv84Uw+OBl+qb+xcbqmAc7k7t+/OHoWZiPlV5LNQw6mYjyHDxy/MabyAD9Y=;t0068lQAAACVn3xoQ8XnCFWg+7cJpfmLdkaOMXKdE9Qq6z0OCfJsKXDovxPL0tWHCnMMoOE03U3ECqr8XzCc0qM/GCe0Lf6M=")
        if error[0] != EnumErrorCode.DBR_OK:
            print("License error: " + error[1])

        # 2.Create an instance of Barcode Reader.
        reader = BarcodeReader.get_instance()
        if reader == None:
            raise BarcodeReaderError("Get instance failed")

        # while True:
        try:
            # Replace by your own image path
            # image_folder = (
            #     os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "images"
            # )

            # for idx, img in enumerate(glob.glob(os.path.join(image_folder, "*.*"))):
            #     print("Test", idx + 1, img)

                # 3. Decode barcodes from an image file
            text_results = reader.decode_file(path)

            # 4.Output the barcode text.
            if text_results != None and len(text_results) > 0:
                for text_result in text_results:
                    print(
                        "Barcode Format : ", text_result.barcode_format_string
                    )
                    print("Barcode Text : ", text_result.barcode_text)
                    print(
                        "Localization Points : ",
                        text_result.localization_result.localization_points,
                    )
                    print("Exception : ", text_result.exception)
                    barcode_data.append(text_result.barcode_text)
                    print("-------------")                    
                    
            print(40 * "#")
            os.remove(path)
            # break
            
        except Exception as e:
            pass
            
        reader.recycle_instance()

    except BarcodeReaderError as bre:
        print(bre)
    
    return barcode_data
