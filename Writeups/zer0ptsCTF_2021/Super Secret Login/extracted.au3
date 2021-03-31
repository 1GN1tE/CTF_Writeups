$hgui = GUICreate("Super Secret Login", 0x160, 0x6d, +0xffffffff, +0xffffffff)
GUISetFont(0x9, 0x190, 0x0, "Courier New")
$hlabel = GUICtrlCreateLabel("Enter Password:", 0x19, 0x19, 0x6d, 0x12)
$hinput = GUICtrlCreateInput("", 0x8c, 0x17, 0xbc, 0x14)
GUICtrlSetFont(+0xffffffff, 0x9, 0x190, 0x0, "Courier New", 0x5)
$hbutton = GUICtrlCreateButton("Login!", 0x7a, 0x47, 0x6d, 0x19)
GUICtrlSetStyle(+0xffffffff, $bs_flat)
$hcaret = _WinAPI_CreateCaret($hgui, 0xa, 0x2)
$mserverkey = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
_WinAPI_ShowCaret($hgui)
GUISetState()
While 0x1
    $hmsg = GUIGetMsg()
    Switch $hmsg
        Case $gui_event_close
            Exit
        Case $hbutton
            ONCLICK()
    EndSwitch
WEnd
Func ONCLICK()
    Local $text = GUICtrlRead($hinput)
    Local $fuckpython = StringLen($text)
    If $fuckpython == 0x0 Then Return
    Local $oldfuck = $fuckpython
    GUICtrlSetState($hbutton, $gui_disable)
    Local $fuck = FUCKIT($text, $mserverkey)
    GUICtrlSetState($hbutton, $gui_enable)
    $fuckpython = "7188bb1563e5702342e22a856ad3df1cfa9729b4115d8cfb1f07a0c6fc916477f02f77d656834379b32e"
    If String(BinaryToString($fuck)) == ("" & $fuckpython) Then
        MsgBox(0x40, "Good Job!", "Read the instructions and see if you can submit It!", 0x0, $hgui)
    Else
        MsgBox(0x40, ":(", "You have a long way to go buddy!" & @CRLF & ":(", 0x0, $hgui)
    EndIf
EndFunc   ;==>ONCLICK
Func FUCKIT($data, $key)
    Local $opcode = "0x5589e56031c081ec00010000880404403d0001000075f531f631db0fb6043401c389f0b92b00000031d2f7f18b45140fbe0c1001cb0fb6db8a0c348a041c880434880c1c83c60181fe0001000075cc31f631d231c942460fb6d28a041401c10fb6c98a1c0c88040c881c1400d80fb6c08b7d0c8a5c37ff8a040431c38b7d08e8100000003b751075cc81c40001000061c9c210005053eb1858c1eb048a1c18885c77fe5b83e30f8a1c18885c77ff58c3e8e3ffffff30313233343536373839616263646566"
    Local $codebuffer = DllStructCreate("byte[" & BinaryLen($opcode) & "]")
    DllStructSetData($codebuffer, 0x1, Binary($opcode))
    Local $buffer = DllStructCreate("byte[" & StringLen($data) & "]")
    DllStructSetData($buffer, 0x1, $data)
    Local $destbuffer = DllStructCreate("char[" & (StringLen($data) * 0x2 + 0x1) & "]")
    DllCall("user32.dll", "none", "CallWindowProc", "ptr", DllStructGetPtr($codebuffer), "ptr", DllStructGetPtr($destbuffer), "ptr", DllStructGetPtr($buffer), "int", StringLen($data), "str", $key)
    Local $ret = DllStructGetData($destbuffer, 0x1)
    $buffer = 0x0
    $codebuffer = 0x0
    Return $ret
EndFunc   ;==>FUCKIT