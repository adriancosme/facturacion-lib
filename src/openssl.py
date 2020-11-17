from io import BytesIO
import tempfile
from M2Crypto import X509
from OpenSSL import crypto
from OpenSSL.crypto import FILETYPE_PEM
from M2Crypto import RSA
from lxml import etree
import platform
import os
import hashlib
import base64


class Openssl:

    def __init__(self):
        self.openssl = 'openssl'

    def get_key(self, keyfile, password):
        options = f"pkcs8 -inform DER -in {keyfile} -outform PEM -passin pass:{password}"
        command = f"{self.openssl} {options}"
        key = os.popen(command).read()
        return key

    def get_no_cert(self, cer):
        cert = X509.load_cert_string(
            base64.decodestring(cer), X509.FORMAT_DER)
        serial = str(u'{0:0>40x}'.format(cert.get_serial_number()))
        return serial.replace('33', 'B').replace('3', '').replace(
            'B', '3').replace(' ', '').replace('\r', '').replace(
            '\n', '').replace('\r\n', '')

    def get_sello(self, key, pwd, xml, cadena):
        key_file = self.base64_to_tempfile(key, '', '')
        (no, pem) = tempfile.mkstemp()
        os.close(no)
        cmd = ('openssl pkcs8 -inform DER -outform PEM'
               ' -in "%s" -passin pass:%s -out %s' % (key_file, pwd, pem))
        os.system(cmd)
        keys = RSA.load_key(pem)
        dom = etree.fromstring(xml.encode('utf-8'))
        xsl_root = etree.parse(cadena)
        xsl = etree.XSLT(xsl_root)
        cadena_original = xsl(dom)
        digest = hashlib.new('sha1', cadena_original).digest()
        return base64.b64encode(keys.sign(digest, "sha1"))

    def base64_to_tempfile(self, b64_str=None, suffix=None, prefix=None):
        """ Convert strings in base64 to a temp file
        @param b64_str : Text in Base_64 format for add in the file
        @param suffix : Sufix of the file
        @param prefix : Name of file in TempFile
        """
        (fileno, file_name) = tempfile.mkstemp(suffix, prefix)
        f_read = open(file_name, 'wb')
        f_read.write(base64.decodestring(b64_str))
        f_read.close()
        os.close(fileno)
        return file_name
