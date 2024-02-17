try:
    #exports to tensorRT
    from ultralytics import YOLO


    model = YOLO('./models/best.pt')

    model.export(format='engine',device=0, imgsz=640)
except Exception as e:
    print(e)
    input("Press Enter to continue...") 
