package main

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"io"
	"os"

	"golang.org/x/crypto/ripemd160"
)

func main() {
	if len(os.Args) < 2 {
		panic("must specify filename argument")
	}

	filename := os.Args[1]

	file, err := os.Open(filename)
	if err != nil {
		panic(err)
	}

	hash := sha256.New()

	data := make([]byte, 1024*1024)
	for {
		n, err := file.Read(data)
		if err == io.EOF {
			break
		} else if err != nil {
			panic(err)
		}

		_, err = hash.Write(data[:n])
		if err != nil {
			panic(err)
		}
	}

	sha256digest := hash.Sum(nil)

	hash = ripemd160.New()
	_, err = hash.Write(sha256digest)
	if err != nil {
		panic(err)
	}

	ripemd160digest := hash.Sum(nil)

	hexdigest := hex.EncodeToString(ripemd160digest)

	fmt.Println(hexdigest)
}
