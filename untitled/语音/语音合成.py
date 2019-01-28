#coding=utf-8
import win32com.client  #系统客户端包


# 示例1--语音合成
Linuxcao = win32com.client.Dispatch("SAPI.SPVOICE")
Linuxcao.Speak("Linuxcao is a good man")
Linuxcao.Speak("Linuxcao is a nice man")
Linuxcao.Speak("Linuxcao is a handsome man")


