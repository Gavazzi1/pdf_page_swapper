# What this does
This Python program pads a given pdf to a multiple of 4 pages and, for every 4 pages in the pdf, swaps pages 2 and 3

# Why?
When printing documents for book binding, I format the document in Word for 8.5x11" paper and print it. 

The resulting document prints in landscape orientation and is formatted so that you would fold the paper along the long edge to form booklets, like so:

```
                                       11"
+---------------------------------------+---------------------------------------+
|                                       |                                       |
|    Lorem ipsum dolor sit amet,        |    nascetur ridiculus mus. Integer    |
|    consectetur adipiscing elit.       |    non tempus risus. Nam nec eros     |
|    Praesent pretium tellus massa,     |    ante. Aenean eget nisi nec nunc    |
|    at eleifend odio laoreet nec.      |    molestie consequat. Vivamus ut     |
|    Donec pharetra risus a dolor       |    urna placerat leo rutrum           |   8.5"
|    accumsan pellentesque. Duis        |    faucibus ut lobortis leo.          |
|    nunc mi, venenatis vitae massa     |    Suspendisse varius, nibh non       |
|    nec, varius luctus lectus. Orci    |    volutpat semper, mauris sapien     |
|    varius natoque penatibus et        |    volutpat quam, quis ullamcorper    |
|    magnis dis parturient montes,      |    enim orci vel nulla.               |
| 16                                    |                                     1 |
+---------------------------------------+---------------------------------------+
```

Note the page numbers. You fold multiple sheets up and sew them together, and the pages in the original document 
are paired up so that when you fold them, the appear in order in the final book.

However, most printer paper is long-grained, meaning it runs along the long side of the paper.

If you fold the page along the middle like in the diagram, you fold against the grain, which makes the pages harder to turn and may make the book deteriorate faster.

You can get short-grained paper from certain online sites, but that's a bit of a hassle.

Instead, I wanted to be able to print the book on 11x17" paper and cut it along the 17" side, thus getting short-grained 11x8.5" paper.

The workflow was this:  
1) Add the text to MS word and format it for book binding  
2) Print to pdf to get a document with the pages layed out like in the diagram above  
3) Print the pdf, adjusting the settings to print on 11x17" paper and print 2 pages per sheet

However, the problem with this is that the page containing sub-pages 1 and 16 will now be printed on the same side of the sheet as the page containing sub-pages 
2 and 15, when they should be back to back for folding.

This program swaps pages 2 and 3 so that when you print on 11x17" paper, the correct pages appear back to back.
