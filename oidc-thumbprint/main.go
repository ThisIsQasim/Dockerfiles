package main

import (
	"crypto/sha1"
	"crypto/tls"
	"fmt"
	"log"
	"net/http"
	"net/url"
	"os"

	"github.com/zitadel/oidc/pkg/client"
)

func fingerprint(address string) string {
	conf := &tls.Config{
		InsecureSkipVerify: true, // as it may be self-signed
	}

	conn, err := tls.Dial("tcp", address, conf)
	if err != nil {
		log.Println("Error in Dial", err)
		return ""
	}
	defer conn.Close()
	cert := conn.ConnectionState().PeerCertificates[0]
	fingerprint := sha1.Sum(cert.Raw)
	return fmt.Sprintf("%x", fingerprint) // to make sure it's a hex string
}

func main() {
	if len(os.Args) == 0 {
		panic(fmt.Errorf("requires argument: OIDC issuer"))
	}

	config, err := client.Discover(os.Args[1], &http.Client{})
	if err != nil {
		panic(err)
	}

	jwks := config.JwksURI
	parsed, err := url.Parse(jwks)
	if err != nil {
		panic(err)
	}

	var address string
	if parsed.Port() != "" {
		address = fmt.Sprintf("%s:%s", parsed.Hostname(), parsed.Port())
	} else {
		address = fmt.Sprintf("%s:443", parsed.Hostname())
	}
	fmt.Println(fingerprint(address))
}
