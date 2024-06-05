import traceback
try:
    raise Exception('This is the error message.')
except:
    errorFile = open('./_11_Debugging/errorInfo.txt', 'w', encoding="UTF-8")
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt.')
