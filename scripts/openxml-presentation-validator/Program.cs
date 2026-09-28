using DocumentFormat.OpenXml.Packaging;
using DocumentFormat.OpenXml.Validation;

if (args.Length == 0)
{
    Console.Error.WriteLine("Usage: validator <pptx> [<pptx> ...]");
    return 2;
}

var validator = new OpenXmlValidator();
var failures = 0;

foreach (var file in args)
{
    Console.WriteLine($"=== {file} ===");
    try
    {
        using var doc = PresentationDocument.Open(file, false);
        var errors = validator.Validate(doc).ToList();
        Console.WriteLine($"Open XML validation errors: {errors.Count}");
        foreach (var error in errors.Take(200))
        {
            Console.WriteLine($"[{error.ErrorType}] {error.Description}");
            Console.WriteLine($"  Part: {error.Part?.Uri}");
            Console.WriteLine($"  Path: {error.Path?.XPath}");
            if (error.Node != null)
                Console.WriteLine($"  Node: {error.Node.LocalName}");
        }
        if (errors.Count > 200)
            Console.WriteLine($"... {errors.Count - 200} further errors omitted");
        if (errors.Count > 0)
            failures++;
    }
    catch (Exception ex)
    {
        Console.WriteLine($"OPEN FAILURE: {ex}");
        failures++;
    }
}

return failures == 0 ? 0 : 1;
