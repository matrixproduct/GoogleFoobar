import base64

MESSAGE = '''GkgABgoTCgUSSFNJSVcIBAQOB1RFUEgVDgMfFggXGhNGT0lTThUcAgQKHhYNV0NWRgoVFQYCGwVG T0lTThkBFRMKFxoLHApRTU9UEgoYBhMXCh4WBwRIVltPVAYHHAAVCgoXVEVQSAQADREaHQNIVltP VAAIFgpRTU9UFQYfSFZbT1QEAB5OURw='''

KEY = 'aossipov'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(c ^ ord(KEY[i % len(KEY)])))

print(''.join(result))