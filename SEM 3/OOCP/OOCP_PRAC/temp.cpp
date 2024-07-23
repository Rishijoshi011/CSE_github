#include <iostream>
#include <hpdf.h> // Include libHaru header

int main()
{
    HPDF_Doc pdf;
    HPDF_Page page;
    HPDF_Font font;
    HPDF_REAL width = 210.0;
    HPDF_REAL height = 297.0;

    // Create a new PDF document
    pdf = HPDF_New(NULL, NULL);
    if (!pdf)
    {
        std::cerr << "Error: Cannot create PDF document" << std::endl;
        return 1;
    }

    // Add a new page to the document
    page = HPDF_AddPage(pdf);

    // Set the page size to A4
    HPDF_Page_SetSize(page, HPDF_PAGE_SIZE_A4, HPDF_PAGE_PORTRAIT);

    // Create a font
    font = HPDF_GetFont(pdf, "Helvetica", NULL);

    // Begin text mode
    HPDF_Page_BeginText(page);

    // Set font and font size
    HPDF_Page_SetFontAndSize(page, font, 12);

    // Set text position
    HPDF_Page_TextOut(page, 50, height - 50, "Hello, PDF!");

    // End text mode
    HPDF_Page_EndText(page);

    // Save the PDF to a file
    if (HPDF_SaveToFile(pdf, "output.pdf") != HPDF_OK)
    {
        std::cerr << "Error: Cannot save PDF file" << std::endl;
        HPDF_Free(pdf);
        return 1;
    }

    // Clean up
    HPDF_Free(pdf);

    return 0;
}
