# Load the fulltext search extension
con.execute("select load_extension('./fts3.so')")
