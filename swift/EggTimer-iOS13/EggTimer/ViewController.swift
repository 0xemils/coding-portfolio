
import UIKit
import AVFoundation



class ViewController: UIViewController {
    
    let eggHardness = ["Soft": 360, "Medium": 560, "Hard": 720]
    
    var timer = Timer()
    var totalTime = 0
    var secondsPassed = 0
    var secondsForLabel = 0
    
    var player: AVAudioPlayer!
    
    
    @IBOutlet weak var progressOfEggs: UIProgressView!
    
    @IBOutlet weak var firstLabel: UILabel!
    
    @IBOutlet weak var labelOfSeconds: UILabel!
    
    @IBAction func hardnessSelected(_ sender: UIButton) {
        
        progressOfEggs.progress = 0.0
        secondsPassed = 0
        

        // when button is pressed timer stops or starts
        timer.invalidate()
        
        let hardness = sender.currentTitle!
        
        firstLabel.text = sender.currentTitle!
        
        
        totalTime = eggHardness[hardness]!
        secondsForLabel = eggHardness[hardness]!
        
        timer = Timer.scheduledTimer(timeInterval: 1.0, target: self, selector: #selector(updateCounter), userInfo: nil, repeats: true)
        
        
        
        
    }
    

    @objc func updateCounter() {
        //example functionality
        if secondsPassed < totalTime {
            
            secondsPassed += 1
            
            let percProgress = Float(secondsPassed) / Float(totalTime)
            progressOfEggs.progress = percProgress
        }
        else {
            timer.invalidate()
            firstLabel.text = "DONE!"
        }
        
        
        
        
        if secondsForLabel > 0 {
            labelOfSeconds.text = "\(secondsForLabel) seconds"
            secondsForLabel -= 1
        }
        else {
            labelOfSeconds.text = "0 seconds"
            playSound()
        }
    }

    
    
    func playSound() {
        let url = Bundle.main.url(forResource: "alarm_sound", withExtension: "mp3")
        
        player = try! AVAudioPlayer(contentsOf: url!)
        
        player.play()
    }
    
    
    

    
}
