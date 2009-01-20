import web
import vendor

urls = (
  '/vendor/new', 'NewVendor',
  '/', 'NewVendor'
)

render = web.template.render('static/', base='site')

app = web.application(urls, globals(), autoreload=True)

class NewVendor:
    def POST(self):
        vendor.create(web.input().vendor)
        raise web.seeother('/')

    def GET(self):
        return render.vendor_form()

if __name__ == '__main__':
    app.run()
