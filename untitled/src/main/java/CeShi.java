

import com.yszhdhy.generator.model.project.Project;
import org.dom4j.DocumentException;

import java.io.FileNotFoundException;

public class CeShi {

    public static void main(String[] args) throws DocumentException, FileNotFoundException {

        Project project = new Project();
        /**
         * localhost 数据库地址
         * 3306 数据库端口号
         * root 用户名
         * 123456 密码
         * generator 数据库名称 （可有可无，没有会根据数据库名称创建，有的话就直接生成表）
         **/
        project.generate("localhost","3306","root","123456","generator");

    }

}
