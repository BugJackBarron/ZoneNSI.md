import asyncio
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://www.zonensi.fr/NSI/Terminale/C02/RecursiviteTris/')
    await page.pdf({
                'path' : 'truc.pdf',
                'scale': 0.85,
                'printBackground': False,
                'displayHeaderFooter': True,
                'headerTemplate': '<span class="date"></span>',
                'footerTemplate': '<span class="title"></span>',
                'landscape': True,
                'pageRanges': '1-3',
                'format': 'A5',
                'margin': {'top' : '1cm', 'left' :'2cm', 'right' :'3cm', 'bottom':'4cm'}
            })
    
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())