import UIKit



// To output all integers from string
extension String {
    var westernArabicNumeralsOnly: String {
        let pattern = UnicodeScalar("0")..."9"
        return String(unicodeScalars
                        .compactMap { pattern ~= $0 ? Character($0) : nil })
    }
}

// Extension to add character spacing in UILabel
extension UILabel {
    func addCharactersSpacing(spacing:CGFloat, text:String) {
        let attributedString = NSMutableAttributedString(string: text)
        attributedString.addAttribute(NSAttributedString.Key.kern, value: spacing, range: NSMakeRange(0, text.count))
        self.attributedText = attributedString
    }
}



class ViewController: UIViewController {

    var passwordGen = PasswordGen()
    
    @IBOutlet weak var lableTextCopy: UILabel!
    @IBOutlet weak var passwordOutputLabel: UILabel!
    @IBOutlet weak var numberOfSymbolsSelection: UISegmentedControl!
    @IBOutlet weak var hardnessSelection: UISegmentedControl!
    @IBOutlet weak var genButtonOutlet: UIButton!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        genButtonOutlet.layer.cornerRadius = 8
        passwordOutputLabel.layer.masksToBounds = true
        passwordOutputLabel.layer.cornerRadius = 8
        
        // Adding character spacing when app starts
        passwordOutputLabel.addCharactersSpacing(spacing: 2, text: passwordOutputLabel.text!)
        
        
        // Tap on lable recognizing code
        let tap = UITapGestureRecognizer(target: self, action: #selector(ViewController.tapFunction))
                passwordOutputLabel.isUserInteractionEnabled = true
                passwordOutputLabel.addGestureRecognizer(tap)
       
    }
    
    
    
    // Lable tap recognizing function
    @IBAction func tapFunction(sender: UITapGestureRecognizer) {
        
        // copying lable text
        if passwordOutputLabel.text != "Your Password Here" {
            UIPasteboard.general.string = passwordOutputLabel.text
            lableTextCopy.text = "Password copied!"
        } else {
            return
        }
        
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.2) {
            self.lableTextCopy.text = "Tap on password to copy"
        }
        
    }
    

    @IBAction func infoPressed(_ sender: UIButton) {
        self.performSegue(withIdentifier: "goToInfo", sender: self)
    }
    
    
    @IBAction func genButton(_ sender: UIButton) {
        
        passwordGen.hardnessSegment = hardnessSelection.selectedSegmentIndex
        passwordGen.passwordPrefix = numberOfSymbolsSelection.titleForSegment(at: numberOfSymbolsSelection.selectedSegmentIndex)
        passwordGen.numberOfSymbols = Int(passwordGen.passwordPrefix!.westernArabicNumeralsOnly) ?? 6
        
        lableTextCopy.text = "Tap on password to copy"
   
        
        genButtonOutlet.layer.borderWidth = 2
        genButtonOutlet.layer.borderColor = CGColor(red: 39/255.0, green: 253/255.0, blue: 186/255.0, alpha: 1)
        passwordOutputLabel.textColor = UIColor(red: 39/255.0, green: 253/255.0, blue: 186/255.0, alpha: 1)
        
        
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.3) {
            self.passwordOutputLabel.textColor = UIColor.black
            self.genButtonOutlet.layer.borderWidth = 0
        }
        
        passwordOutputLabel.text = passwordGen.generatePassword()
        
        
    }
    

}

