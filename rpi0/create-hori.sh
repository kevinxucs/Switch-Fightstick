#!/bin/bash

set -x

GADGET="/sys/kernel/config/usb_gadget"

mkdir -p $GADGET/hori
cd $GADGET/hori

echo 0x0F0D > idVendor
echo 0x0092 > idProduct
echo 0x0100 > bcdDevice
echo 0x0200 > bcdUSB
echo 0x00 > bDeviceClass
echo 0x00 > bDeviceSubClass
echo 0x00 > bDeviceProtocol

mkdir -p strings/0x409
echo "0123456789" > strings/0x409/serialnumber
echo "HORI CO.,LTD." > strings/0x409/manufacturer
echo "POKKEN CONTROLLER" > strings/0x409/product

mkdir -p configs/c.1/strings/0x409
echo 0x80 > configs/c.1/bmAttributes
echo 500 > configs/c.1/MaxPower

mkdir -p functions/hid.usb0
echo 0 > functions/hid.usb0/protocol
echo 0 > functions/hid.usb0/subclass
echo 64 > functions/hid.usb0/report_length
echo '05010905a101150025013500450175019510050919012910810205012507463b017504950165140939814265009501810126ff0046ff0009300931093209357508950481020600ff0920950181020a212695089102c0' | xxd -r -ps > functions/hid.usb0/report_desc
ln -s functions/hid.usb0 configs/c.1/

echo "$(ls /sys/class/udc | head -1)" > UDC
