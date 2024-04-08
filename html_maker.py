
# creamos nuestra función  para almacenar todo lo referente a cada ave

def make_cols3(photos):
  
  cols_3 = ''
  for photo in photos:
    cols_3 += f'''
    <div class="col-3">
      <div class="card>
        <imgclass="w-100" src="{photo[url]}" alt="">
        <h4>{photo['title']}</h4>
        </div>
      </div>
    '''
  return cols_3


def make_full_html(cols_3):
  html_completo = f'''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Bootstrap demo</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
      </head>
      <body>
        <h1 class="text-center">Blog simple</h1>
        <div class="container">
        <div class="row"
          <!-- Acá van las col-3's-->
          {cols_3}
        </div>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
      </body>
    </html>

    '''
  return html_completo