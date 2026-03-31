package programmingtheiot.unit.system;

import static org.junit.Assert.*;

import java.util.logging.Logger;

import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;

import programmingtheiot.gda.system.SystemCpuUtilTask;
import programmingtheiot.gda.system.SystemDiskUtilTask;
public class SystemDiskUtilTaskTest {
    //static 
    private static final Logger _Logger = 
        Logger.getLogger(SystemDiskUtilTask.class.getName());

    //member var's 
    private SystemDiskUtilTask diskUtilTask = null; 

    // test setup methods
	
	/**
	 * @throws java.lang.Exception
	 */
	@BeforeClass
	public static void setUpBeforeClass() throws Exception
	{
	}
	
	/**
	 * @throws java.lang.Exception
	 */
	@AfterClass
	public static void tearDownAfterClass() throws Exception
	{
	}
	
	/**
	 * @throws java.lang.Exception
	 */
	@Before
	public void setUp() throws Exception
	{
		this.diskUtilTask = new SystemDiskUtilTask();
	}
	
	/**
	 * @throws java.lang.Exception
	 */
	@After
	public void tearDown() throws Exception
	{
	}
	
	// test methods
	
	/**
	 * Test method for {@link programmingtheiot.gda.system.SystemCpuUtilTask#getTelemetryValue()}.
	 */
	@Test
	public void testGetTelemetryValue()
	{
		float diskUtil  = 0.0f;
		int   totTests = 5;
		
		
		
		for (int i = 1; i <= totTests; i++) {
			diskUtil = this.diskUtilTask.getTelemetryValue();
			if (diskUtil >= 0.0f) {
				_Logger.info("Test " + i + ": Disk Utilization: " + diskUtil + "GB");
				assertTrue(diskUtil >= 0.0f);

			} else {
				_Logger.warning("Failed to retrieve disk utilization.");
			}
		}
	}

	@Test
	public void testGetAllDiskData(){
		for (int = 0; i <)
	}

}
