package main

import (
	"errors"
	"fmt"
	"io"
	"os/exec"
)


func main()  {
	dateCmd := exec.Command("date")

	dateOut, err := dateCmd.Output()
	if err != nil {
		panic(err)
	}

	fmt.Println("> date")
	fmt.Println(string(dateOut))

	_, err = exec.Command("date", "-x").Output()

	if err != nil{
		var execErr *exec.Error
		var exitErr *exec.ExitError
		if errors.As(err, &execErr) {
			fmt.Println("failed executing:", execErr)
		}else if errors.As(err, &exitErr){
			exitCode := exitErr.ExitCode()
			fmt.Println("command exit -rc", exitCode)
		}else{
			panic(err)
		}
	}

	grepCmd := exec.Command("grep", "hello")

	grepIn, _ := grepCmd.StdinPipe()
	grepOut, _ := grepCmd.StdoutPipe()
	grepCmd.Start()
	grepIn.Write([]byte("hello grep\ngoodbye grep"))
	grepIn.Close()
	grepByte, _ := io.ReadAll(grepOut)
	grepCmd.Wait()

	fmt.Println("> grep hello")
	fmt.Println(string(grepByte))

	lsCmd := exec.Command("bash", "-c", "ls -a -l -h")
	lsOut, err := lsCmd.Output()
	if err != nil {
		panic(err)
	}
	fmt.Println("> ls -a -l -h")
	fmt.Println(string(lsOut))

}