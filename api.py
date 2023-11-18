import os

import requests
from pprint import pprint

import requests


cookies=  {
    'OTDefaultLang': 'en-us',
    's_fid': '3C516184BAF51C16-1A0C264EDE8E2F33',
    'OTLang': 'en',
    'akacd_us1': '3874454926~rv=13~id=aa33882aace5f4435bd32fbbfaceebf4',
    'brandingid': '12',
    's_cc': 'true',
    'Login': 'LoginURL=%2F&LastLoginName=invoices.finkraft.ai%40tatacommunications.com',
    'bm_sz': '7F62CD20EC8031D88C101E5D686B46D0~YAAQbAosFzsic8+LAQAAL/m13BW8MaKxeuJxiwQS0Dq6Hv2aRBBXBecmoMjhXYUuYUd5yGK9KsZ/yyMNco9Z4yOiZXQu2S2pIleTrY0biTOYGscw0PO0OlaJVWi5q0URktklFFoA0H+8POLoEnNLMaUnTL322EGD0WhK3ci2/mwYjzrjEbYHp6TsK3SvYQu2E234PctWeJWOZZS5wx+TVoE2oJpy6n0suqCMNUmyPwuwOKwTWfrqifuXzdGmxHrwDf29q/yw92SiwgjlZTWPjCZb5ijkkNeqOQ146UqnArznNu9WMCu4zchItLg=~4601651~3687478',
    'OTSESSIONAABQRN': '0C74BC02G096EG47D7G9493GA28868AAF850',
    'OTSESSIONAABQRD': '0C74BC02G096EG47D7G9493GA28868AAF850',
    'JWT': 'eyJraWQiOiIxNDU1NjE0MDIyIiwiYWxnIjoiUlMyNTYiLCJ0eXAiOiJKV1QifQ.eyJjb25jdXIuc2NvcGVzIjpbIioiXSwiYXVkIjoiKiIsImNvbmN1ci5hcHBJZCI6IjRjYjhjYzYyLWE3MTMtNGEyOC04Y2UwLTRkOTZmNzhjOTgwMyIsInN1YiI6IjI1MGQ0Y2VmLWU1YTQtNDg1YS1hZjJhLWIwMTE4Njk3YzUyOSIsImlzcyI6Imh0dHBzOi8vdXMyLmFwaS5jb25jdXJzb2x1dGlvbnMuY29tIiwiY29uY3VyLnByb2ZpbGUiOiJodHRwczovL3VzMi5hcGkuY29uY3Vyc29sdXRpb25zLmNvbS9wcm9maWxlL3YxL3ByaW5jaXBhbHMvMjUwZDRjZWYtZTVhNC00ODVhLWFmMmEtYjAxMTg2OTdjNTI5IiwiZXhwIjoxNzAwMjE4ODA2LCJjb25jdXIudmVyc2lvbiI6MywiY29uY3VyLnR5cGUiOiJ1c2VyIiwiY29uY3VyLmFwcCI6Imh0dHBzOi8vdXMyLmFwaS5jb25jdXJzb2x1dGlvbnMuY29tL3Byb2ZpbGUvdjEvYXBwcy80Y2I4Y2M2Mi1hNzEzLTRhMjgtOGNlMC00ZDk2Zjc4Yzk4MDMiLCJuYmYiOjE3MDAyMTUxOTYsImNvbmN1ci5jb21wYW55IjoiNzUyYmIxYzQtNDFlZC00NzM3LWFlZDctM2U5NGRlZjkzY2E3IiwiaWF0IjoxNzAwMjE1MjA2fQ.eWn-wpLMCbtKVB9kBbe4Ku9WxVfpBHL0Zo80Xlpw5VOrZDCKYRVJAYuXlzp-hJ292gUxX69IasmBRXRPDeOu6h3BWjfyAc5n25VnGI2Jg7zk-fUlg070u8fOJPWlEZOq5FlLshAeHQ33i67bdcINh8-bJIy9tRBS11j81tIMtvyFzFEwAGpBDGEe2r-7gHlnB7xPFhhtfkNItscNg-lncP7K_JcbXabuwiKRn-QXuTgja1u382lLtL1N1UsBSkV8sXIQ5PjVTLX4N2Np-Tm_RqzYlr1o-toxhtolBt5ptHjmJzo5h12XjYyHu_qhwg7oAsCUQq5JhRwHfowNw-uVbA',
    'bm_mi': '3100D61E59BE8C3DD79F44A734349062~YAAQbAosF9Rrc8+LAQAAXD653BXZnSyGqm8hs1TU0cFDSjhSNwR/EmeMe6jf42Cxsr6CtNDPmF5d4r36orvjT/wh+iybyxKbRYdGcLDJ/t+ziKa7DJLQl4LwpRmNU3vadtw287IKKo9D2HARBvZEhju1NuqRbDoaxkkUTjFMPez2lkK6iVx9LBN8cFjAO3ZqhW6VOilukGtvpyejATRXuSVV5E6EYOMWBu1zezUnYBHkaDMG+9DlGvDwA+rIB1Uo8peRig9U4zNP0hvP6SIvI9GlOCYgrDxDfezEgc8zbT3ZHPcRctsAQFhBWfszaIvupax7gX+I/DDU+793~1',
    'ak_bmsc': 'FB6A444B489A541C8AB57A211D5B44C7~000000000000000000000000000000~YAAQbAosF/Ztc8+LAQAAyFG53BUxuXutK/TqYyKqZ3jzf/vRxjkXBkR5H/idYG9hZ5OnoQpYDfYHDXdX09urm0Hd8nU7rKP+rKjQ7VCgZBP5FfgG6oGs1vI4YyZ3trWFA6pPd2X2uCawtOQK+6qf5Rnymo6uxHpuc96G9Hd9Ybyz755zLgbOU5/a2nCgYPhqcG61vbhDsINNHJpZttUtAK3s3XDqDlk0bw2vBDMNazYgJSTv1gO1/+Zu3x4NrcJVVEu/2s7mW2ko92ZHnjSYMgpcuV0K0qkkydhO5athi1vRSzFxAddmv976XulpET/dqmMrMSR6lZwBYl4N5wH7yN44UOUFFLmRsTjId53G21uwK88Mzswx+QjTuNKgydLzaN+ZafHIlGfH20wFhKEaKAxXA2mN6EvUga7Su6tXM+XIJdpua2U3LA2vehCTsahkBFZaWO01hOz0z0w6yH0lXhewuYVYiQtnOeiq35s67g==',
    'TAsessionID': '79327f8f-1ee7-47bb-ac59-bbb3af533393|NEW',
    'CteMtRequestId': '11%2F17%2F2023%2D18015%2E68',
    'bm_sv': '28D8941D78E351EBD69B83F93DEFBB6E~YAAQzuvfrVjdcdyLAQAADm253BV30Jdxg2oCeoRj0Yr+MlQiPOwUnp+mw23D/TyuVXRuP2G+rtwnBXtXvFuOWT4ZC1GheJ4Lfmq5Uh1DBjR8eTqS1/pzL3qGfc+Ot3rFZcGxz7NYNZ0HlkquwtIFxSDXIxWMnFs9pvRXy+DnKhR2KUW1KKeCuaMZnqev5/JZWzp0SrqNbwvIXzW4AVdFanYX2yKM8xZc3Ct+vRQCsBun3CoPMSxtFyyQO6Sq9x3c8PgvUDOWzbI3~1',
    '_abck': '863CF018E9FAB5EABC757144BE9C2F7F~-1~YAAQbAosF5/LdM+LAQAALobG3ArmQQRfvgNd1qQkH//TUqbY2PUEG4wHL1IWrjcpN9NcDDdTKqVkJqd2Kpevm9sgi0Jvr/+mbV82t3IFu5V4bqkaqDr25fzb3h1y8toc8xunp1eqftLU/cM0JzPIrIHCtVl5Z2YQ9o//9+kdze5cflnII5jY1yFihU6tCMaGxpuNK446T7CX7pWgJzE9zQxyVeL1AHHBs1ava53AxkK15V1bV6kwlk22lbBIMqtT7NF+7BkCXwAjmTJGA7a3lnZQDofhuEQRyyPHleCzP4bLQ45WgQ0BsR/OgLkudNscQNzqkA/KgJB7r3V0m21R0Hgtat8K+NiikgE31a8A+ES//24bnahfOB3PcDGMcNuAZB8kc0VrCKlzk9g85/VK7dAhDA==~-1~-1~-1',
    'AWSALBTG': 'EEp7ZMmQ/o7XtVMLRShoVyASG3fE8AGfwaDgj2A6VMiguFFErYygwOvIsdJ52XoId0eqFuISPy6A8eXL0KPTQtQpVEFdaFrp3pTgkzM7IU83kktZ5tnZoOwE1KlSPmwNnqlV+IPurTT2s8kFesdqEthgD8LttDyKdvD+qpkGwLVDCuSAErZ+OkswvEaTlkobOMmUtadGcaZTlNFKceh4h024QuhVLbmbK0ieaRU/LVfVHCA5+jaxgwuq478ztFk20LbvpXhqDl5s4Q==',
    'AWSALBTGCORS': 'EEp7ZMmQ/o7XtVMLRShoVyASG3fE8AGfwaDgj2A6VMiguFFErYygwOvIsdJ52XoId0eqFuISPy6A8eXL0KPTQtQpVEFdaFrp3pTgkzM7IU83kktZ5tnZoOwE1KlSPmwNnqlV+IPurTT2s8kFesdqEthgD8LttDyKdvD+qpkGwLVDCuSAErZ+OkswvEaTlkobOMmUtadGcaZTlNFKceh4h024QuhVLbmbK0ieaRU/LVfVHCA5+jaxgwuq478ztFk20LbvpXhqDl5s4Q==',
}


headers = {
    'authority': 'www.concursolutions.com',
    'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'OTLang=en-gb; akacd_us1=3875059595~rv=98~id=47d9a14703dbe7c166828e2d0bf1a5a0; brandingid=12; OTDefaultLang=en-us; s_fid=3804F4A1D05BE0AC-2D9129CE29DA3AC6; s_cc=true; bm_sz=6E8477B7FA72A0F962C505B591774581~YAAQFCozagCDHDmLAQAApom4QxWbyahrsaOoUVNlviN4LmuT/JNGTgVK5P65lzyBCWGEUzedGoApRYQcAd7yHsVvj67joJMdYiO2lXb/bo486JiFtF+NF3mFLpACNtIorlSHN/1oI/VQG5L78E06zTuHCEZCT2e141/hhB5yL4SXQDQSk53XI2soSLJdVL2qlPwmDlsBcP5dwf8yF39jMWMIBvoeRAlI89lrk0MeqnEfQ40tSis9Hqk7zKuuiRNZ96QR98Cbtydd4NsUoHDjvZYZg8wHkoLX0DXZQ0b2r3o9D9xMD62L8U2PDf8=~3223607~3356985; bm_mi=4774F6C582F9621C17002A8685C86D19~YAAQxkYDF7fiKj6LAQAA7kAKRBWCFG7lMdMdYXIUgOFzciztvPdtyUrQhYwL3t0nA6Sfqk8/wgeZILLI5UDWw7kw7tTvlb8WngqJLURPs+wxYHRe9204FN1uRpUiQ4VRAWYcZZafRsPblaAP9ELAoW9aLyvBy14Nw2wYB248wvCH+FD2JSDKfAqhVnYVTMTTTaZgPrNmgVLNxcx9OHnbM3fKV4FnMviMKjScHxqOHMKXFeTJXeA/vjRbgNHG7dC0pjgjuI7WZCzmJvId0MJYMLhW0x4poBn186ku7ITDZooTYocjque711leO3RzKu7+DiyvIwJUdK04KBy6Emle1zU=~1; TAsessionID=3cb2b852-c2e7-49df-8ff5-a87f09619594|NEW; ak_bmsc=C8923608CA259005D16AA994DA14AE3D~000000000000000000000000000000~YAAQxkYDF8fiKj6LAQAAG0QKRBU4NztgprU2rf7rUV6c1kom7s0QXXa5NiMXtkMhph7Sf4dRborUBtUZhAuY+Fk4gZc5i/txY28M9dI17wxJXoONfEMI8rQD0GPZkrwx3hJivoa1l8IXwjrtgOun+HQ0/+YYdH6HgPIF8HSRNChgYX8XBwcLXiHQRi5L1MvKwgk59IySxDxCzEJAj/KWGiTOHJ4Cg6XeIieSOW4V83VYG7VnZjBSwWWsnqJ+oEk+HAaK8srEHfdShjLhmMFwcaLe5QXd7mFBMNvKBZtq8dqaM96d1IdOPo60DE0wVR98k5onLBCf3eSKKHvuyypfB6SS4PaOfmosPcT91KjrkAgX0oJKiglrtZRME65v/R7c0PDBZA78NsjFVwZnB23aj9AxRNU+VDVuAihkkUe6ylKHdKdUQ4W7A0EUk63s5oA/OMqOYtIJ+MbdF2coZ7LX/7lFqyK1iI0vUkzbidMwJpGRHzQeH5DCU3IOQjjhlwnvYCfVmZkn1ucg053CqQKqQ3TLSY6BPzseFnZR2q1oVpN95Z1vPrTthh7mISjcmyEfa9GUkXP0lbdmZ8qDIQfBgkBrdkcrD7M1USzE; OTSESSIONAABQRN=9CB7C593GD850G47FDGA6AAG4790577B5D17; OTSESSIONAABQRD=9CB7C593GD850G47FDGA6AAG4790577B5D17; JWT=eyJraWQiOiIxNDU1NjE0MDIyIiwiYWxnIjoiUlMyNTYiLCJ0eXAiOiJKV1QifQ.eyJjb25jdXIuc2NvcGVzIjpbIioiXSwiYXVkIjoiKiIsImNvbmN1ci5hcHBJZCI6IjRjYjhjYzYyLWE3MTMtNGEyOC04Y2UwLTRkOTZmNzhjOTgwMyIsInN1YiI6IjI1MGQ0Y2VmLWU1YTQtNDg1YS1hZjJhLWIwMTE4Njk3YzUyOSIsImlzcyI6Imh0dHBzOi8vdXMyLmFwaS5jb25jdXJzb2x1dGlvbnMuY29tIiwiY29uY3VyLnByb2ZpbGUiOiJodHRwczovL3VzMi5hcGkuY29uY3Vyc29sdXRpb25zLmNvbS9wcm9maWxlL3YxL3ByaW5jaXBhbHMvMjUwZDRjZWYtZTVhNC00ODVhLWFmMmEtYjAxMTg2OTdjNTI5IiwiZXhwIjoxNjk3NjU3MjU2LCJjb25jdXIudmVyc2lvbiI6MywiY29uY3VyLnR5cGUiOiJ1c2VyIiwiY29uY3VyLmFwcCI6Imh0dHBzOi8vdXMyLmFwaS5jb25jdXJzb2x1dGlvbnMuY29tL3Byb2ZpbGUvdjEvYXBwcy80Y2I4Y2M2Mi1hNzEzLTRhMjgtOGNlMC00ZDk2Zjc4Yzk4MDMiLCJuYmYiOjE2OTc2NTM2NDYsImNvbmN1ci5jb21wYW55IjoiNzUyYmIxYzQtNDFlZC00NzM3LWFlZDctM2U5NGRlZjkzY2E3IiwiaWF0IjoxNjk3NjUzNjU2fQ.tVSrCpspWbCDqDbdfGncC7P6zbUH9YDiIfFrrM3aFMbGEpBP9b1lBbTeRR62HkxsukoLnXptaCNQ5K-j4m8MwEvgEUA4r2GO7kdJ0VjnLJMQe7W4FV8K8HNaaWj0uXnzJoZJQbtbdtZIO4GsUjxy5IGU6Fcc3nZbOA4n0rdlbFCnOstFacqNpDW5aDKracXTWyv8MjJolxemSlGW8qUHeod-LMXu6bt2zsdvbv1Bfc3UmeEFSPTves79rULK1pDEZSYIGVI13bJqCmyijb5YwWxH23tJG4Nmh87PY2TBDbnWwY2Rn5ST6PR5QCfoSeyQokyG7Ew80mWLW6D6dViDVQ; bm_sv=54925541821F5C323D5B51E0C9ADF110~YAAQRq1NaA2dTzSLAQAAPh4LRBU50aE+H+lLp04aSPVgoa8qWnyzWBIfhxOVTq8p1E+1mrp++GOFwE0V/EvPu8EKzWWZw5WbIFDue8FkpbW8ngDh+pbe6cBlA5Abkd1ejeuHc4wYijJT+tPPI6GR0eWi21mBmiqQTRnfv0qEJNT2c0drirYwPLi4ntP6ywNh8zaWGKq3Tx+gt399OqpG+zRObsVrnEnWSZPT9NP6lc8RlAg6OU9mwNc0NGHs2RxeQGIx0jGwNNkU~1; CteMtRequestId=10%2F18%2F2023%2D52063%2E05; AWSALBTG=Y+UeBNoPxoFI9R5/4/Fqfo/2Ai067ts5NYwsKiVhonutBD+Yn+Rq8frlXBqS5g3ypvYOESvXzTLfPq3ogAI1WUOS2uEIFoYlHlkZV3zKv5pKwONhZBwARpBmA8GmQsohXhcO+M53ED93INmsaTdpVEPUrNJOp1SQJHdSdkx3V9SkDF0+jw75ilJ+CPLjsWryHAtFOlYR4pt8IVTBwPu9G7X+21zF3s3hJ//R2ZG/gR82aKypygOxv9Rjtst5/oyOhdmhzsXaWEWYwQknAYhj2lrQ0b/maBSv/QwDId2Z9+bAE9Jnj++L3juiKYyEklAzPV9qrzMhQ3h6GkTw8VIvXVjL7P3xMYFgdlCo29KZPGwA4a0K6yh8fRJHJ5spGgNon8SZibRBHSTDYbHu+3rGCTv2Aj8uS855bQj7OoqzVxMZ1XeoUSpPAlbM2AWXt6Hwyu0=; AWSALBTGCORS=Y+UeBNoPxoFI9R5/4/Fqfo/2Ai067ts5NYwsKiVhonutBD+Yn+Rq8frlXBqS5g3ypvYOESvXzTLfPq3ogAI1WUOS2uEIFoYlHlkZV3zKv5pKwONhZBwARpBmA8GmQsohXhcO+M53ED93INmsaTdpVEPUrNJOp1SQJHdSdkx3V9SkDF0+jw75ilJ+CPLjsWryHAtFOlYR4pt8IVTBwPu9G7X+21zF3s3hJ//R2ZG/gR82aKypygOxv9Rjtst5/oyOhdmhzsXaWEWYwQknAYhj2lrQ0b/maBSv/QwDId2Z9+bAE9Jnj++L3juiKYyEklAzPV9qrzMhQ3h6GkTw8VIvXVjL7P3xMYFgdlCo29KZPGwA4a0K6yh8fRJHJ5spGgNon8SZibRBHSTDYbHu+3rGCTv2Aj8uS855bQj7OoqzVxMZ1XeoUSpPAlbM2AWXt6Hwyu0=; _abck=ADF0DD2A1283D0B91944F5EEDF67F4B9~-1~YAAQxkYDF5PpKj6LAQAAsuALRArFLdALM4xPwnZYHuHu+nRNhalM6BYksxhqmqLWP+Wd0tsFA14Z5dbPO5EFa/poXQA3Zwa6H9kS5NCU/2mhBXZzmEPyAfTCZ5jnuuVCe3etvxjnDCIB1NHwmvjKB+8xHpXzHM1CwbdE25YMjlrOxyEa740llDuz1SSUOoDv10zJ9UM08+kUgZc8Q3Xg3IJSxGNCbuEbkHUUVDhDDnvoBuRx+Vp5dRopsasqozs1pavYkX8V2KtjzGozJbQtDhKv499OC+wwxNslzdJeAkP954rJ4NPlsblKquyVsoM+31zuuwnU+OuCsHZjUVfPB0OkSgIFqQNYbNEejlgg7mSFb15aDHzAfKmrzh3AvihvUc+VxVcU+Q3LRLIdP36RcuO+Dg==~-1~-1~-1',
    'origin': 'https://www.concursolutions.com',
    'referer': 'https://www.concursolutions.com/Expense/Client/processor.asp',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'x-prototype-version': '1.6.1',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'requests': 'ExpenseReport:GetProcessorReportsList',
}

data = {
    'data': '[{"action":"ExpenseReport","method":"GetProcessorReportsList","data":[1702,"ACCT_AUDIT_MGR","Y","","N","Search","","","Y",1010,"",1500,2000,"","","2022-04-01 00:00:00.0","after","CT_REPORT","SUBMIT_DATE","TIMESTAMP","","","","","",""]}]',
    '_': '',
}

response = requests.post(
    'https://www.concursolutions.com/expense/expenseDotNet/Proxy/expenseRouter.ashx',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)

data = response.json()
rpts = data['ExpenseReport_GetProcessorReportsList']['Body']['rpts']['rpt']
params = {
    'requests': 'ExpenseEntry:GetExpenseEntries,ExpenseReport:GetReportHeader,ExpenseEntry:GetAuthRequestsForRpt,ExpenseEntry:GetAuthRequestEntriesForRpt',
}
#
# data = {
#      'data': '[{"action":"ExpenseEntry","method":"GetExpenseEntries","data":["gWmyiLLNqx2fRvLZy9F3SxftPuECOdRFA","","N","Y",1053,"ACCT_AUDIT_MGR",1021]},{"action":"ExpenseReport","method":"GetReportHeader","data":["gWmyiLLNqx2fRvLZy9F3SxftPuECOdRFA",1053,"ACCT_AUDIT_MGR"]},{"action":"ExpenseEntry","method":"GetAuthRequestsForRpt","data":["gWmyiLLNqx2fRvLZy9F3SxftPuECOdRFA"]},{"action":"ExpenseEntry","method":"GetAuthRequestEntriesForRpt","data":["gWmyiLLNqx2fRvLZy9F3SxftPuECOdRFA"]}]',
#     '_': '',
# }
# RptKey,
#print(rpts[0])

pdf_files = []
write_header = True
for rpt in rpts:
    rpt_key=rpt.get("RptKey")
    data=[{"action":"ExpenseEntry","method":"GetExpenseEntries","data":["gWmyiLLNqx2fRvLZy9F3SxftPuECOdRFA","","N","Y",1053,"ACCT_AUDIT_MGR",1021]},{"action":"ExpenseReport","method":"GetReportHeader","data":["gWmyiLLNqx2fRvLZy9F3SxftPuECOdRFA",1053,"ACCT_AUDIT_MGR"]},{"action":"ExpenseEntry","method":"GetAuthRequestsForRpt","data":["gWmyiLLNqx2fRvLZy9F3SxftPuECOdRFA"]},{"action":"ExpenseEntry","method":"GetAuthRequestEntriesForRpt","data":["gWmyiLLNqx2fRvLZy9F3SxftPuECOdRFA"]}]
    for d in data:
        d['data'][0] = rpt_key
    # data = {'action': 'ExpenseReport', 'method': 'GetReportHeader', 'data': ['%s' % (rpt_key), 1053, 'ACCT_AUDIT_MGR']}
    new_data = {}
    new_data['data'] = str(data)
    response = requests.post(
        'https://www.concursolutions.com/expense/expenseDotNet/Proxy/expenseRouter.ashx',
        params=params,
        cookies=cookies,
        headers=headers,
        data=new_data,
    )
    data = response.json()

    expense_entries = data['ExpenseEntry_GetExpenseEntries']['Body']['ExpenseEntries']['Records']
    for expense in expense_entries:
        rc_id = expense.get('ReceiptImageId', None)
        if rc_id is None:
            continue
        expense_name = expense.get("ExpName")

        params_pdf = {
            'requests': 'Receipts:GetLineItemImage',
        }
        p_data = [{"action":"Receipts","method":"GetLineItemImage","data":["D4861C99AB484885AFAE19F36B69BBAC","N"]}]
        p_data[0]["data"][0] = "%s"%(rc_id)
        data_pdf = {}
        data_pdf["data"] = str(p_data)

        response = requests.post(
            'https://www.concursolutions.com/expense/expenseDotNet/Proxy/expenseRouter.ashx',
            params=params_pdf,
            cookies=cookies,
            headers=headers,
            data=data_pdf,
        )
        payload = response.text
        import re

        # pattern = r'"thumbUrl":\s*"([^"]*)"'
        pattern = r'url:\s*"([^"]*)"'

        # Use re.search to find the match

        match = re.search(pattern, payload)

        # Check if a match was found
        thumb_url = None
        if match:
            thumb_url = match.group(1)  # Extract the thumbUrl value
            # print("Thumb URL:", thumb_url)
            pdf_files.append({"expense_name":expense_name, "url": thumb_url})
        else:
            print("ThumbUrl not found in the JSON text.")

        if thumb_url is None:
            continue
        import csv

        with open('pdf_data3.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)

            # Writing the header row
            if write_header:
                writer.writerow(['Expense Name', 'Invoice URL'])
                write_header = False

            # Writing multiple rows of data

            writer.writerow([expense_name, thumb_url])
        # print("expenseeeeeee", expense_name)
        # if expense_name == "Lodging":
            try:
                folder = "./sap_100"
                local_file = f"{folder}/expense_{rc_id}.pdf"
                response = requests.get(thumb_url)
                with open(local_file, 'wb') as pdf_file:
                    pdf_file.write(response.content)
                print(f"PDF saved locally as {local_file}")

            except Exception as e:
                print(f"Error downloading PDF: {str(e)}")




