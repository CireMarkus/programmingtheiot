package programmingtheiot.gda.system;

import java.util.logging.Logger;
import java.io.File;


import programmingtheiot.common.ConfigConst;

public class SystemDiskUtilTask extends BaseSystemUtilTask {
	private File drive = new File(ConfigConst.ROOT_DIR);
	private long totalSpaceGB = drive.getTotalSpace() / (1024 * 1024 * 1024);
	private long freeSpaceGB = drive.getFreeSpace() / (1024 * 1024 * 1024);
	private long usableSpaceGB = drive.getFreeSpace() / (1024 * 1024 * 1024);
	private long usedSpaceGB = totalSpaceGB - freeSpaceGB;

	private static final Logger _Logger = 
		Logger.getLogger(SystemDiskUtilTask.class.getName());
    
	public SystemDiskUtilTask(){
		super(ConfigConst.NOT_SET, ConfigConst.DEFAULT_TYPE_ID);
	}

	@Override
	public float getTelemetryValue() {
		//returns the total used space in gigabytes for the root dir of the project. 
		return (float) usedSpaceGB;
	}

	public void getAllDiskData(){
		_Logger.info("--- Disk Usage for " + drive.getAbsolutePath() + " ---");
		_Logger.info("Total Space: " + totalSpaceGB + " GB");
        _Logger.info("Free Space: " + freeSpaceGB + " GB");
        _Logger.info("Usable Space (for JVM): " + usableSpaceGB + " GB");
        _Logger.info("Used Space: " + usedSpaceGB + " GB");
	}
}
