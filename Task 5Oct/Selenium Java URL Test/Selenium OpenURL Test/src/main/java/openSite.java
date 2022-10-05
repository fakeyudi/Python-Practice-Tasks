import static org.junit.Assert.*;

import com.selenium.test.webtestsbase.BasePage;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.junit.Test;
import org.openqa.selenium.safari.SafariDriver;

import java.util.concurrent.TimeUnit;


public class openSite {
    @Test
    public void openGoogleAndSearch() {
        WebDriver browser;
        //System.setProperty("webdriver.gecko.driver", "/usr/local/Cellar/geckodriver/0.31.0/bin/geckodriver");
       // /usr/local/bin/chromedriver
        //browser = new FirefoxDriver();
        browser = new ChromeDriver();
        browser.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
        browser.get("https://www.google.com/");
        WebElement searchBar = browser.findElement(By.name("q"));
        searchBar.sendKeys("BYJU'S");
        searchBar.sendKeys(Keys.ENTER);
        browser.close();
    }
}
