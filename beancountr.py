#!/usr/bin/env python

import web
import vendor, receipt

urls = (
  '/b/latest', 'Latest',
  '/b/vendors', 'VendorList',
  '/b/vendor/new', 'NewVendor',
  '/b/receipt/new', 'NewReceipt',
  '/b', 'NewReceipt'
)

render = web.template.render('static/', base='site')

app = web.application(urls, globals(), autoreload=True)

class Latest:
    def GET(self):
        return render.receipt_list(receipt.getLatest())

class VendorList:
    def GET(self):
        return render.vendor_list(vendor.getAll())

class NewVendor:
    def POST(self):
        vendor.create(web.input().vendor)
        raise web.seeother('/')

    def GET(self):
        return render.vendor_form()

class NewReceipt:
    def POST(self):
        input = web.input()
        receipt.create(dict(vendor=input.vendor, damage=input.damage, \
          date=input.date))
        raise web.seeother('/')

    def GET(self):
        return render.receipt_form(vendor.getAll())

if __name__ == '__main__':
    app.run()
